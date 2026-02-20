from flask import Blueprint, render_template, request, jsonify
from src.services.articulos_lista_service import articulos_lista_service

articulos = Blueprint("articulos", __name__)

@articulos.route("/articulos")
def articulos_page(): 
    lista_articulos = articulos_lista_service(0)
    return render_template("articulos.html", lista_articulos=lista_articulos)

