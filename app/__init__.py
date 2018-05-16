from app.doc import TEMPLATE
from app.model import Mongo
from app.view import Router
from config import Config

from flasgger import Swagger
from flask import Flask
from flask_cors import CORS


def create_app():
    instance = Flask(__name__)
    instance.config.from_object(Config)

    Swagger(template=TEMPLATE).init_app(instance)
    Router().init_app(instance)
    Mongo().init_app(instance)
    CORS().init_app(instance)

    return instance


app = create_app()
