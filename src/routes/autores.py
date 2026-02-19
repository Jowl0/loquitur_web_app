from flask import Blueprint, render_template, request, jsonify

from src.services.obtener_autores import obtener_autores
autores = Blueprint("autores", __name__)

@autores.route("/autores")
def autores_page(): 
    lista_autores=obtener_autores(0,10)
    return render_template("autores.html",autores=lista_autores)