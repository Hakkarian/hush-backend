from __main__ import app

@app.route("/gallery", methods=["POST"])
def create_user():
    print("hererere")
    d = request.json
    all_users.append(d)
    print(d)
    return jsonify(all_users), 201