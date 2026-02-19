from flask import Blueprint, render_template, request, jsonify
from src.services.obtener_articulos import obtener_articulos_paginados

articulos = Blueprint("articulos", __name__)

@articulos.route("/articulos")
def articulos_page(): 
    lista_articulos = obtener_articulos_paginados(0)
    return render_template("articulos.html", lista_articulos=lista_articulos)

