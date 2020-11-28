from flask import Flask

from delivery.extensions import admin, auth, cli, config, db, migrate, site


def create_app():
    """Create main factory"""

    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    site.init_app(app)
    return app
