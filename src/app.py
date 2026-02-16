from flask import Flask, send_from_directory
from src.config import Config
from src.database.db import db
import src.models 
from src.routes import register_blueprints



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_blueprints(app)

    @app.route("/articulos/<path:filename>")
    def serve_articulos(filename):
        return send_from_directory(
            app.config["ARTICULOS_DIR"],
            filename
        )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)