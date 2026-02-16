import os

from flask import Flask, render_template, send_from_directory
from flask_minify import Minify

import articulos

app = Flask(__name__)
Minify(app=app, html=True, js=True, cssless=True)


@app.route("/articulos/<path:filename>")
def serve_articulos(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    articulos_path = os.path.join(root_dir, "articulos")
    # Es importante que el nombre de la carpeta coincida exactamente
    return send_from_directory(articulos_path, filename)


@app.route("/")
def hello():
    grid = articulos.grid()
    print(grid)
    return render_template("home.html", grid=grid)


app.run(debug=True)
