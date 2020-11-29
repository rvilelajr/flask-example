from delivery.extensions.auth.controller import create_user, save_user_photo
from delivery.extensions.auth.form import UserForm
from flask import Blueprint, redirect, render_template, request

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/restaurants")
def restaurants():
    return render_template("restaurants.html")


@bp.route("/signup", methods=["POST", "GET"])
def signup():
    form = UserForm()
    if form.validate_on_submit():
        create_user(
            email=form.email.data,
            password=form.password.data,
            name=form.name.data,
        )
        photo = request.files.get("photo")
        if photo:
            save_user_photo(photo.filename, photo)
        return redirect("/")

    return render_template("userform.html", form=form)
