from src.database import db

class edicion_articulo(db.Model):
    __tablename__ = "edicion_articulo"
    edicion_id = db.Column(db.Integer, db.ForeignKey("ediciones.id"), primary_key=True)
    articulo_id = db.Column(db.Integer, db.ForeignKey("articulos.id"), primary_key=True)
    orden_en_edicion = db.Column(db.Integer, nullable=False)
    __table_args__ = (
        db.UniqueConstraint(
            "edicion_id", "orden_en_edicion", name="uq_orden_por_edicion"
        ),
    )