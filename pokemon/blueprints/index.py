


def init_app(app):
    @app.route('/')
    def index():
        return {'message': 'hello world'}
