from src.database import db

class autor(db.Model):
    __tablename__ = "autores"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True)
    instagram_url = db.Column(db.String(255))
    fecha_registro = db.Column(
        db.String(19), nullable=False, default=db.func.datetime("now")
    )