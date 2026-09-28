from flask import Flask

from app.controllers.auth_controller import auth_bp
from app.middleware.auth_middleware import auth_middleware


app = Flask(
    __name__,
    template_folder="views",
    static_folder="static"
)

app.secret_key = "chave-secreta-teste"

app.register_blueprint(auth_bp)

app.before_request(auth_middleware)