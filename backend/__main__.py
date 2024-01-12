from dotenv import load_dotenv
load_dotenv()
from flask import jsonify, request, Response
from flask_cors import CORS

from backend import create_app
from backend.cloudinary.cloudinary_config import configure_cloudinary, fetch_store_pictures, retrieve_pictures
from backend.routes.health import health_bp
from backend.routes.gallery import gallery_bp


app = create_app()
CORS(app)

configure_cloudinary()
# fetch_store_pictures(cursor)

app.register_blueprint(health_bp)
app.register_blueprint(gallery_bp)



if __name__ == "__main__":
    app.run(host='127.0.0.1')
