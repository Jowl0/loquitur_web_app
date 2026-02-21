from .home import home
from .articulos import articulos
from .error_404 import error_404
#from .ver_mas import ver_mas_api
from .quienes_somos import quienes_somos
from .autores import autores
from .perfil_autor import perfil_autor
from .articulo import articulo
from .ver_mas_articulos_api import ver_mas_articulos_api
from .ver_mas_articulos_autor_api import ver_mas_articulos_autor_api


def register_blueprints(app):
    app.register_blueprint(home)
    app.register_blueprint(articulos)
    app.register_blueprint(error_404)
   # app.register_blueprint(ver_mas_api)
    app.register_blueprint(quienes_somos)
    app.register_blueprint(autores)
    app.register_blueprint(perfil_autor)
    app.register_blueprint(articulo)
    app.register_blueprint(ver_mas_articulos_api)
    app.register_blueprint(ver_mas_articulos_autor_api)