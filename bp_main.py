from flask import Blueprint, render_template, redirect, url_for, session

main_bp = Blueprint("main", __name__)
@main_bp.route("/")
def inicio():
    if "usuario" not in session: # si no ha iniciado sesión...
       return redirect(url_for("auth.login")) # ...lo mandamos al login
    return render_template("bienvenida.html", usuario=session["usuario"])