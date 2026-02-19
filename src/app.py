from flask import Flask, send_from_directory
from src.config import Config
from src.database.db import db
import src.models 
from src.routes import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.secret_key = 'una_clave_muy_secreta_y_unica'
    with app.app_context():
        db.create_all()

    register_blueprints(app)

    @app.route("/media/<path:filename>")
    def serve_articulos(filename):
        
        return send_from_directory(
        app.config["MEDIA_DIR"],
        filename
    )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)