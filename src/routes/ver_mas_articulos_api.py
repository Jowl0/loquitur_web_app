from flask import Blueprint, request, jsonify
from src.services.articulos_lista_service import articulos_lista_service

ver_mas_articulos_api = Blueprint("ver_mas_articulos_api", __name__)

@ver_mas_articulos_api.route("/api/ver_mas/articulos", methods=['GET'])
def ver_mas_articulos_api_route():
    contador = request.args.get('contador', 1, type=int)
    articulos = articulos_lista_service(contador=contador)
    
    return jsonify(articulos)