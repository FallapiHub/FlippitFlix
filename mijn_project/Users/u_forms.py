from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, TextAreaField, PasswordField


class Voeguser(FlaskForm):




    user_name = StringField('Users name: ')
    user_email = EmailField("Users email: ")
    user_password = PasswordField("Password: ")
    submit = SubmitField('Add user: ')