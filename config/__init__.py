import os


class Config:
    DEBUG = False

    REMOTE_HOST = None
    PORT = 5000

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

        'host': '{}:{}'.format(REMOTE_HOST, PORT) if REMOTE_HOST else None,
        'basepath': '/'
    }


