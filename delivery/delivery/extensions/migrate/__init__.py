from flask_migrate import Migrate
from delivery.extensions.db import db
from delivery.extensions.db import models


migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)