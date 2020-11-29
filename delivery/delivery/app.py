from flask import Flask

from delivery.extensions import config


def create_app():
    """Create main factory"""

    app = Flask(__name__)
    config.init_app(app)

    return app
