from flask import Flask


def create_app():
    """Create main factory"""

    app = Flask(__name__)
    views.init_app(app)
    return app
