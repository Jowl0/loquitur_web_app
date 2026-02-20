from flask import Blueprint, render_template
import src.services
quienes_somos = Blueprint("quienes_somos", __name__)

@quienes_somos.route("/quienes_somos", methods=['GET'])
def quienes_somos_page():
    return render_template("quienes_somos.html")
