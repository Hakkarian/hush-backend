from flask import Blueprint, jsonify, request, Response
from io import BytesIO
from PIL import Image
import base64
import cloudinary.uploader
import cloudinary.api

from backend.config.postgre_config import configure_postgresql
from backend.config.weaviate_config import create_weaviate, store_photo, search_similar

gallery_bp = Blueprint("gallery", __name__, url_prefix="/gallery")

conn, cursor = configure_postgresql()

@gallery_bp.route("", methods=["GET"])
def get_all_pics():
    cursor.execute("""SELECT * FROM pictures""")

    pics = cursor.fetchall()

    conn.commit()

    return jsonify(pics)

@gallery_bp.route("/add", methods=["POST"])
def create_picture():
    print("1")

    file = request.files['image']
    print("2")
    result = cloudinary.uploader.upload(file)
    print("3")
    url = result['url']
    print("4")
    id = result['public_id']
    print("5")
    cursor.execute("""
        INSERT INTO pictures (cloudinary_url, cloudinary_id) VALUES (%s, %s)
    """, (url, id))

    store_photo(url)
    print("6")
    conn.commit()

    return jsonify("yas"), 201

@gallery_bp.route("/similar", methods=["POST"])
def similar(): 
    uploaded_file = Image.open(request.files['image'].stream)
    buffer = BytesIO()
    uploaded_file.save(buffer, format="JPEG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    weaviate_results = search_similar(img_str)

    images = []
    for idx, obj in enumerate(weaviate_results):
        result = obj["image"]
        # create a file with the result inside, similar to writeFileSync(path, result, "base64")
        file_path = f"result_{idx}.jpg"
        with open(file_path, "wb") as file:
            file.write(base64.b64decode(result))

        images.append(file_path)
    return jsonify(images), 201

@gallery_bp.route("/createw", methods=["GET"])
def weaviate():
    create_weaviate()
    return jsonify("Class has been created succesfully")

@gallery_bp.route("/remove", methods=["POST"])
def remove_picture():
    req = request.json
    id = req.get("public_id")
    print('removable id', id)

    cloudinary.uploader.destroy(id)

    cursor.execute("""
        DELETE FROM pictures WHERE cloudinary_id = %s
     """, (id,))

    conn.commit()
    return jsonify("Picture has been deleted succesfully")