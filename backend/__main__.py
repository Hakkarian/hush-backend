from flask import jsonify, request, Response

from backend import create_app

app = create_app()

@app.route("/health", methods=["GET"])
def health_check():
    return "ok"

@app.route("/gallery", methods=["GET"])
def get_all_users():
    all_users = [{"id": 1, "name": "daniel"}, {"id": 2, "name": "bob"}]
    return jsonify(all_users)

@app.route("/gallery", methods=["POST"])
def create_user():
    print("hererere")
    d = request.json
    all_users.append(d)
    print(d)
    return jsonify(all_users), 201


if __name__ == "__main__":
    app.run(host='127.0.0.1')
