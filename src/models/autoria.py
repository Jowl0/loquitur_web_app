from src.database import db

class autoria(db.Model):
    __tablename__ = "autoria"
    articulo_id = db.Column(db.Integer, db.ForeignKey("articulos.id"), primary_key=True)
    autor_id = db.Column(db.Integer, db.ForeignKey("autores.id"), primary_key=True)
    rol = db.Column(db.String(20), nullable=False, default="Autor")