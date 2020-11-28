from delivery.extensions.admin import admin as admin_ext
from delivery.extensions.auth import models  # noqa
from delivery.extensions.auth.admin import UserAdmin
from delivery.extensions.auth.models import User
from delivery.extensions.db import db


def init_app(app):
    """TODO: initialize Flask Simple Login + JWT"""

    admin_ext.add_view(UserAdmin(User, db.session))
