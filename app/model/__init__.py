from mongoengine import *


class Mongo(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        mongo = app.config['MONGO']
        connect(mongo['db'], host=mongo['host'], port=mongo['port'])
