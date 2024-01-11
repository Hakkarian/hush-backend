from __main__ import app

@app.route("/gallery", methods=["GET"])
def get_all_users():
    all_users = [{"id": 1, "name": "daniel"}, {"id": 2, "name": "bob"}]
    return jsonify(all_users)