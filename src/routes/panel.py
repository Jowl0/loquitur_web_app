# src/routes/panel.py
from flask import Blueprint, redirect, url_for
from flask_login import current_user

admin_panel_bp = Blueprint("admin_panel", __name__, url_prefix="/admin")

@admin_panel_bp.before_request
def verificar_sesion():
    if not current_user.is_authenticated:
        return redirect(url_for("auth_admin.admin_login"))

@admin_panel_bp.route("/")
def panel_admin():
    return f"<h1>Bienvenido al panel admin, {current_user.email}</h1>"