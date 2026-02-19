from .home import home
from .articulos import articulos
from .error_404 import error_404
from .ver_mas import ver_mas_api
from .quienes_somos import quienes_somos
from .autores import autores
from .perfil_autor import perfil_autor


def register_blueprints(app):
    app.register_blueprint(home)
    app.register_blueprint(articulos)
    app.register_blueprint(error_404)
    app.register_blueprint(ver_mas_api)
    app.register_blueprint(quienes_somos)
    app.register_blueprint(autores)
    app.register_blueprint(perfil_autor)