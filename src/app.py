from flask import Flask, send_from_directory
from flask_login import LoginManager
from src.config import Config
from src.database.db import db
from src.routes import register_blueprints
from src.models.admin import admin

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = '123'

    db.init_app(app)

    # Configuración de Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    # Asegúrate de que esto apunte a tu blueprint de login correctamente
    login_manager.login_view = "auth_admin.admin_login" 

    @login_manager.user_loader
    def load_user(user_id):
        # 1. Usamos query.get directamente sobre el modelo
        return admin.query.get(int(user_id))

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