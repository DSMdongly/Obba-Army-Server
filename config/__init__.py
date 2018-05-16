import os


class Config:
    DEBUG = False
    REMOTE_HOST = 'https://obba-army.herokuapp.com'

    HOST = 'localhost'
    PORT = os.getenv('PORT', 5000)

    SERVICE_NAME = 'obba-army'
    SECRET = os.getenv('SECRET_KEY', '78OC34B1ABC11263A357R8FBM99Y7221D7DB')

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs/'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': 'Obba Army Backend API Spec'
        },

        'host': '{}'.format(REMOTE_HOST) if REMOTE_HOST else None,
        'basepath': '/'
    }

    if REMOTE_HOST is None:
        SWAGGER['host'] = '{}:{}'.format(HOST, PORT)

    MONGO = {
        'host': 'ds111420.mlab.com',
        'port': 11420,
        'db': '{}'.format(SERVICE_NAME),
        'username': 'gdh0608',
        'password': 'kim0608'
    }



