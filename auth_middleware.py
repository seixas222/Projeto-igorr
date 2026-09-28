from flask import session, request, redirect, url_for


def auth_middleware():

    rotas_publicas = [
        "auth.login",
        "static"
    ]

    if request.endpoint in rotas_publicas:
        return

    if "usuario" not in session:
        return redirect(url_for("auth.login"))