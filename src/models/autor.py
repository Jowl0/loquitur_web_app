from src.database import db

class autor(db.Model):
    __tablename__ = "autores"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True)
    instagram_url = db.Column(db.String(255))
    correo_url = db.Column(db.String(255))
    linkedin_url = db.Column(db.String(255))
    x_url = db.Column(db.String(255))
    url_imagen = db.Column(db.String(800), nullable=False)
    url_pagina = db.Column(db.String(800), nullable=False)
    fecha_registro = db.Column(
        db.String(19), nullable=False, default=db.func.datetime("now")
    )