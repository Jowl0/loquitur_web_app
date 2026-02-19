from flask import Blueprint, render_template
import src.services
quienes_somos = Blueprint("quienes_somos", __name__)

@quienes_somos.route("/quienes_somos", methods=['GET'])
def quienes_somos_page():
    grid=src.services.get_grid()
    lista_articulos = src.services.obtener_articulos_paginados(0)
    
    return render_template("quienes_somos.html", grid=grid, lista_articulos=lista_articulos)
