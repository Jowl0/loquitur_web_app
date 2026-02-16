from src.database import db

class imagen(db.Model):
    __tablename__ = "imagenes_articulo"
    id = db.Column(db.Integer, primary_key=True)
    articulo_id = db.Column(db.Integer, db.ForeignKey("articulos.id"), nullable=False)
    url = db.Column(db.String(800), nullable=False)
    posicion = db.Column(db.Integer, nullable=False)
    __table_args__ = (
        db.CheckConstraint("posicion BETWEEN 1 AND 3", name="ck_posicion_1_3"),
        db.UniqueConstraint("articulo_id", "posicion", name="uq_articulo_posicion"),
    )