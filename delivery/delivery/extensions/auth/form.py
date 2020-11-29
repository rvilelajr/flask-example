import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField


class UserForm(FlaskForm):
    email = wtf.StringField(
        "Email", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    password = wtf.PasswordField("Password", [wtf.validators.DataRequired()])
    name = wtf.StringField("Name", [wtf.validators.DataRequired()])
    photo = FileField("Photo")
