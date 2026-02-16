from flask import Blueprint, render_template,request
from src.database.db import db
from src.models.articulo import articulo
from src.models.imagen import imagen

home = Blueprint("home", __name__)

@home.route("/")
def home_page():
    grid = (
    db.session.query(articulo.titulo, imagen.url,articulo.slug)
    .join(imagen, imagen.articulo_id == articulo.id)
    .filter(imagen.posicion == 1)
    .filter(articulo.estatus=='publicado')
    .order_by(articulo.fecha_creacion.desc())
    .limit(5)
    .all()
    )   

    lista_articulos=(
    db.session.query(articulo.titulo, imagen.url, articulo.descripcion, articulo.fecha_publicacion,articulo.slug)
    .join(imagen, imagen.articulo_id == articulo.id)
    .filter(imagen.posicion == 1)
    .filter(articulo.estatus=='publicado')
    .order_by(articulo.fecha_creacion.desc())
    .limit(5)
    .all()
    )  
    print(lista_articulos)
    print(grid)

    return render_template("home.html",grid=grid,lista_articulos=lista_articulos)
