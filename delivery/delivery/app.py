from flask import Flask
from delivery.extensions import site
from delivery.extensions import config
from delivery.extensions import db
from delivery.extensions import cli


def create_app():
    """Create main factory"""

    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    site.init_app(app)
    return app
