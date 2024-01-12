from flask import Blueprint, jsonify, request, Response

gallery_bp = Blueprint("gallery", __name__, url_prefix="/gallery")

@gallery_bp.route("", methods=["GET"])
def get_all_users():
    all_users = [{"id": 1, "name": "daniel"}, {"id": 2, "name": "bob"}]
    return jsonify(all_users)

@gallery_bp.route("", methods=["POST"])
def create_user():
    print("hererere")
    d = request.json
    all_users.append(d)
    print(d)
    return jsonify(all_users), 201