from src.database import db
from flask_login import UserMixin

# 1. Agregamos UserMixin a la herencia
class admin(db.Model, UserMixin):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    contrasena = db.Column(db.String(800), nullable=False) 

# 2. Sacamos la función de la clase y devolvemos el objeto completo
def admin_id_db(id):
    return admin.query.get(int(id))