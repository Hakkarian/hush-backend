from flask import Blueprint, jsonify, request, Response
import cloudinary.uploader

from backend.config.postgre_config import configure_postgresql
from config.weaviate_config import create_weaviate


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
    print("6")
    conn.commit()

    return jsonify("yas"), 201

@gallery_bp.route("/createw", methods=["POST"])
    const req = requst.json
    schema_config = req.get("schema_config")
    create_weaviate(schema_config)
    return jsonify("Class has been created succesfully")

@gallery_bp.route("/remove", methods=["POST"])
def remove_picture():
    req = request.json
    url = req.get("url")
    print('removable image', url)
    cursor.execute("""
        DELETE FROM pictures WHERE cloudinary_url = %s
     """, (url,))

    conn.commit()
    return jsonify("Picture has been deleted succesfully")