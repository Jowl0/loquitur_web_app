from flask import Blueprint, render_template
from src.database.db import db
from src.models.articulo import articulo
from src.models.imagen import imagen

articulos = Blueprint("articulos", __name__)
@articulos.route("/articulos")
def home_page():
  
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

    return render_template("articulos.html",lista_articulos=lista_articulos)