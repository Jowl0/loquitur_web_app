# src/routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from src.models.admin import admin 

# El nombre del blueprint aquí es "auth_admin"
auth_admin_bp = Blueprint("auth_admin", __name__)

@auth_admin_bp.route("/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        usuario = admin.query.filter_by(email=email).first() 
        
        if usuario and check_password_hash(usuario.contrasena, password):
            login_user(usuario)
            # Verifica que el nombre del blueprint en panel.py coincida con "admin_panel"
            return redirect(url_for("admin_panel.panel_admin"))

        flash("Credenciales inválidas.")
        return redirect(url_for("auth_admin.admin_login")) # Nombre interno del BP

    return render_template("login.html")

# --- Nueva ruta de Logout ---
@auth_admin_bp.route("/logout")
@login_required
def admin_logout():
    logout_user()
    flash("Has cerrado sesión correctamente.") # Opcional: un mensaje de feedback
    return redirect(url_for("auth_admin.admin_login"))