from flask import Blueprint, render_template, request, jsonify, abort
from src.services import obtener_autor
from src.services import obtener_articulos_paginados
perfil_autor = Blueprint("perfil_autor", __name__)

@perfil_autor.route("/autores/<autor>/")
def perfil_autor_page(autor):
    autor_data=obtener_autor(autor)
    if autor_data:
        articulos_lista=obtener_articulos_paginados(0,autor_id=autor_data[0]['id'])
    #print(articulos)
    if not autor_data:
        abort(404)
    return render_template("perfil_autor.html",autor=autor_data,articulos=articulos_lista)