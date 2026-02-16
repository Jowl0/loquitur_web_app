from .home import home
from .articulos import articulos
from .error_404 import error_404

def register_blueprints(app):
    app.register_blueprint(home)
    app.register_blueprint(articulos)
    app.register_blueprint(error_404)