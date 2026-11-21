from flask import Blueprint, render_template, request
from flask import redirect, url_for, session
from werkzeug.security import check_password_hash
from usuarios import USUARIOS

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    mensaje = ""
    if request.method == "POST":
       usuario = request.form["usuario"]
       contrasena = request.form["contrasena"]
       # 1) ¿Existe el usuario?
       if usuario in USUARIOS:
          # 2) ¿La contraseña coincide con su hash guardado?
          if check_password_hash(USUARIOS[usuario], contrasena):
             session["usuario"] = usuario # guardamos quién entró
             return redirect(url_for("main.inicio"))
       # Si llegamos aquí, algo estuvo mal
       mensaje = "Usuario o contraseña incorrectos"

    return render_template("login.html", mensaje=mensaje)

@auth_bp.route("/logout")
def logout():
    session.pop("usuario", None) # borramos la sesión
    return redirect(url_for("auth.login"))