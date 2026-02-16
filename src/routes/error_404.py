from flask import Blueprint, render_template


error_404 = Blueprint("404", __name__)

@error_404.app_errorhandler(404)
def _404(error):
    return render_template("404.html"), 404