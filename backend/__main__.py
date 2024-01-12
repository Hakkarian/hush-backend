from dotenv import load_dotenv
load_dotenv()
from flask import jsonify, request, Response
from flask_cors import CORS

from backend import create_app
from backend.cloudinary.cloudinary_config import configure_cloudinary, fetch_store_pictures, retrieve_pictures
from backend.postgresql.postgre_config import configure_postgresql

app = create_app()
CORS(app)

configure_cloudinary()
conn, cursor = configure_postgresql()
# fetch_store_pictures(cursor)





@app.route("/health", methods=["GET"])
def health_check():
    return "ok"

if __name__ == "__main__":
    app.run(host='127.0.0.1')
