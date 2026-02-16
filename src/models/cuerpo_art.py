from src.database import db

class cuerpo_art(db.Model):
    __tablename__ = "cuerpo_articulo"
    id = db.Column(db.Integer, primary_key=True)
    articulo_id = db.Column(db.Integer, db.ForeignKey("articulos.id"), nullable=False)
    ruta = db.Column(db.String(800), nullable=False)  # Ruta del html
    version = db.Column(db.Integer, nullable=False, default=1)
    fecha_creacion = db.Column(
        db.String(19), nullable=False, default=db.func.datetime("now")
    )
    __table_args__ = (
        db.UniqueConstraint(
            "articulo_id", "version", name="uq_cuerpo_articulo_version"
        ),
    )