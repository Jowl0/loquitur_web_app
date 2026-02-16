from src.database import db


class edicion(db.Model):
    __tablename__ = "ediciones"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    mes = db.Column(db.Integer, nullable=False)
    estatus = db.Column(db.String(20), nullable=False, default="draft")
    fecha_salida = db.Column(db.String(10))
    fecha_creacion = db.Column(
        db.String(19), nullable=False, default=db.func.datetime("now")
    )
    __table_args__ = (db.UniqueConstraint("anio", "mes", name="uq_edicion_anio_mes"),)
