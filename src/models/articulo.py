from src.database import db

class articulo(db.Model):
    __tablename__ = "articulos"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(300), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    slug = db.Column(db.String(300), unique=True, nullable=False)
    estatus = db.Column(db.String(20), nullable=False, default="draft")
    fecha_publicacion = db.Column(db.String(19))
    fecha_programacion = db.Column(db.String(19))
    fecha_creacion = db.Column(
        db.String(19), nullable=False, default=db.func.datetime("now")
    )
    ultima_actualizacion = db.Column(
        db.String(19), nullable=False, default=db.func.datetime("now")
    )
