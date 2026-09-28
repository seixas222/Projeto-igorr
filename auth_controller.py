from flask import Blueprint, render_template, request
from flask import redirect, url_for, session

from app.models.user_model import verificar_usuario


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if verificar_usuario(username, password):

            session["usuario"] = username

            return redirect(url_for("auth.home"))

        return render_template(
            "login.html",
            erro="Usuário ou senha incorretos."
        )

    return render_template("login.html")


@auth_bp.route("/home")
def home():

    return render_template(
        "home.html",
        usuario=session.get("usuario")
    )


@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))