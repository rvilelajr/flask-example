import os

from delivery.extensions.auth.models import User
from delivery.extensions.db import db
from flask import current_app as app
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename


def create_user(email, password, name, admin=False):
    user = User(
        email=email,
        password=generate_password_hash(password, "pbkdf2:sha256"),
        name=name,
        admin=admin,
    )
    db.session.add(user)
    db.session.commit()

    return user


def save_user_photo(filename, filestorage):
    """
    Saves user photo
    ./uploads/{user}/filename.ext
    """
    filename = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(filename))
    filestorage.save(filename)
