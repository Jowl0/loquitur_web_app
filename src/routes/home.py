from flask import Blueprint, render_template, request, jsonify
import src.services

home = Blueprint("home", __name__)

@home.route("/", methods=['GET'])
def home_page():
    grid=src.services.get_grid()
    lista_articulos = src.services.obtener_articulos_paginados(0)
    
    return render_template("home.html", grid=grid, lista_articulos=lista_articulos)
