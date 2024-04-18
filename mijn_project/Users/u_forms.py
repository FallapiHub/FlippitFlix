from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from mijn_project.models import Users


class LoginForm(FlaskForm):
    user_email = StringField('Email:', validators=[DataRequired(), Email()])
    user_password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Log in')


class Voeguser(FlaskForm):




    user_name = StringField('Username:', validators=[DataRequired()])
    user_email = EmailField("Email:", validators=[DataRequired(),Email()])
    user_password = PasswordField("Password:", validators=[DataRequired(), EqualTo("pass_confirm",    message='Passwords Must Match!')])
    pass_confirm = PasswordField("Confirm Password:", validators=[DataRequired()])
    submit = SubmitField('Add user')

    def check_email(self, field):
        if Users.query.filter_by(user_email=field.data).first():
            raise ValidationError('This email addres is already registered')

    def check_username(self, field):
        if Users.query.filter_by(user_name=field.data).first():
            raise ValidationError('This username is already taken!')


