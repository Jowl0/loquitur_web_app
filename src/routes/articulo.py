from flask import Blueprint, render_template, request, jsonify, abort
from src.services.articulo_service import articulo_service
from src.services.autor_service import autor_service

articulo = Blueprint("articulo", __name__)

@articulo.route("/articulos/<articulo_slug>/")
def articulo_pagina(articulo_slug):
    articulo_data = articulo_service(articulo_slug)
    print(articulo_data)
    if not articulo_data:
        abort(404)
        
    autor_data = autor_service(articulo_id=articulo_data["id"])
        
    return render_template(
        'articulo_1.html', 
        articulo=articulo_data, 
        autor=autor_data
    )