from flask import Blueprint, jsonify, request, Response

from backend.postgresql.postgre_config import configure_postgresql

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

    req = request.json
    url = req.get("url")
    id = req.get("id")

    cursor.execute("""
        INSERT INTO pictures (cloudinary_url, cloudinary_id) VALUES (%s, %s)
    """, (url, id))

    conn.commit()

    return jsonify("yas"), 201

@gallery_bp.route("/remove", methods=["POST"])
def remove_picture():
    req = request.json
    url = req.get("url")
    cursor.execute("""
        DELETE FROM pictures WHERE cloudinary_url = %s
     """, (url,))

    conn.commit()
    return jsonify("Picture has been deleted succesfully")