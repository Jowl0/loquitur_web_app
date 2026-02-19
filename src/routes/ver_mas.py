from flask import Blueprint, request, jsonify
from src.services.obtener_articulos import obtener_articulos_paginados

ver_mas_api = Blueprint("ver_mas_api", __name__)

@ver_mas_api.route("/api/ver_mas", methods=['GET'])
def api_ver_mas():
    contador = request.args.get('contador', 1, type=int)
    autor_id = request.args.get('autor_id', type=int)
    try:
        resultado = obtener_articulos_paginados(contador, 5, autor_id=autor_id)
        print(f"DEBUG: Contador: {contador}, Autor: {autor_id}, Resultados: {len(resultado)}")
        return jsonify(resultado)
    
    except Exception as e:
        print(f"Error en API: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500