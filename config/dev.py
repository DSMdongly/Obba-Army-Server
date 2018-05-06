from config import Config


class DevConfig(Config):
    DEBUG = True
    HOST = 'localhost'

    if not Config.REMOTE_HOST:
        Config.SWAGGER['host'] = '{}{}'.format(HOST, Config.PORT)

    MONGO = {
        'host': 'localhost',
        'port': 27017,
        'db': '{}-dev'.format(Config.SERVICE_NAME)
    }
