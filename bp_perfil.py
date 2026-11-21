# bp_perfil.py -&gt; Blueprint de PERFIL
from flask import Blueprint, render_template, redirect, url_for, session

profile_bp = Blueprint("perfil", __name__)

@profile_bp.route("/perfil")
def perfil():
    if "usuario" not in session:
        return redirect(url_for("auth.login"))
    return render_template("perfil.html", usuario=session["usuario"])