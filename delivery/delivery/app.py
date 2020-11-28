from flask import Flask
from delivery.extensions import site


def create_app():
    """Create main factory"""

    app = Flask(__name__)
    site.init_app(app)
    return app
