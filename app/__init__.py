from app.doc import TEMPLATE
from app.model import Mongo
from app.view import Router

from config.dev import DevConfig
from config.prod import ProdConfig

from flasgger import Swagger
from flask import Flask


def create_app(dev=True):
    instance = Flask(__name__)
    instance.config.from_object(DevConfig if dev else ProdConfig)

    Swagger(template=TEMPLATE).init_app(instance)
    Router().init_app(instance)
    Mongo().init_app(instance)

    return instance


app = create_app(False)
