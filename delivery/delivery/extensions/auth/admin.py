from delivery.extensions.auth.models import User
from delivery.extensions.db import db
from flask import flash
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView


def format_name(obj, request, user, *args):
    return user.name.capitalize()


class UserAdmin(ModelView):
    """Admin user interface"""

    column_formatters = {"name": format_name}
    column_list = ["name", "email", "admin"]
    # can_edit = False

    column_searchable_list = ["email"]

    column_filters = ["admin"]

    @action(
        "toggle_admin",
        "Toggle admin flag",
        "Are you sure?",
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin

        db.session.commit()
        flash(f"{len(users)} Users updated successfully", "success")
