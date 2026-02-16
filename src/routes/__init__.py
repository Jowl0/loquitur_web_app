from .home import home
from .articulos import articulos

def register_blueprints(app):
    app.register_blueprint(home)
    app.register_blueprint(articulos)