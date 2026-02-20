from flask import Blueprint, render_template, request, jsonify, abort
from src.services.autor_service import autor_service
from src.services.articulos_lista_autores_service import articulos_lista_autor_service
perfil_autor = Blueprint("perfil_autor", __name__)

@perfil_autor.route("/autores/<autor>/")
def perfil_autor_page(autor):
    autor_data=autor_service(slug=autor)
    if autor_data:
        articulos_lista=articulos_lista_autor_service(autor_data[0]['id'], 0)
    print(autor_data)
    if not autor_data:
        abort(404)
    return render_template("perfil_autor.html",autor=autor_data,articulos=articulos_lista)