class Router:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from app.view import music_chart
        app.register_blueprint(music_chart.api.blueprint)
