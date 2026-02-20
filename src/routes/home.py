from flask import Blueprint, render_template, request, jsonify
from src.services.grid_service import grid_service
from src.services.articulos_lista_service import articulos_lista_service

home = Blueprint("home", __name__)

@home.route("/", methods=['GET'])
def home_page():
    grid=grid_service()
    lista_articulos = articulos_lista_service(0)
    
    return render_template("home.html", grid=grid, lista_articulos=lista_articulos)
