from flask import Flask, Response, request, current_app
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from os import environ


def check_credentials(username, password):
    config_username = current_app.config.get(
        "BASIC_AUTH_USERNAME", environ.get("BASIC_AUTH_USERNAME", None)
    )
    config_password = current_app.config.get(
        "BASIC_AUTH_PASSWORD", environ.get("BASIC_AUTH_PASSWORD", None)
    )
    return username == config_username and password == config_password


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if (
            not auth
            or not auth.username
            or not auth.password
            or not check_credentials(auth.username, auth.password)
        ):
            return Response("Login Required!", 401, {"WWW-Authenticate": 'Basic realm="Login!"'})
        return f(*args, **kwargs)

    return wrapper
