from config import Config


class ProdConfig(Config):
    DEBUG = False
    HOST = 'localhost'

    if not Config.REMOTE_HOST:
        Config.SWAGGER['host'] = '{}{}'.format(HOST, Config.PORT)

    MONGO = {
        'host': 'localhost',
        'port': 27017,
        'db': '{}-dev'.format(Config.SERVICE_NAME),
        'username': 'gdh0608',
        'password': 'kim0608'
    }