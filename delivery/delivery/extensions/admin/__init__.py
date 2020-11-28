from delivery.extensions.db import db
from delivery.extensions.db.models import Category
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin()


def init_app(app):
    admin.name = "Delivery Admin"
    admin.template_mode = "bootstrap2"
    admin.init_app(app)

    admin.add_view(ModelView(Category, db.session))
