from flask import Blueprint, render_template, request, jsonify
from src.services.autores_service import autores_service

autores = Blueprint("autores", __name__)

@autores.route("/autores")
def autores_page(): 
    lista_autores=autores_service(0,10)
    return render_template("autores.html",autores=lista_autores)