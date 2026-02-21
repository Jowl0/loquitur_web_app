from flask import Blueprint, request, jsonify
from src.services.articulos_lista_autores_service import articulos_lista_autor_service

ver_mas_articulos_autor_api = Blueprint("ver_mas_articulos_autor_api", __name__)

@ver_mas_articulos_autor_api.route("/api/ver_mas/articulos/autor", methods=['GET'])
def ver_mas_articulos_autor_api_route():
    contador = request.args.get('contador', 1, type=int)
    id_autor = request.args.get('id_autor', type=int)

    articulos = articulos_lista_autor_service(id_autor, contador, 5)
    
    return jsonify(articulos)