import os
from flask import Flask, Blueprint, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mijngeheimesleutel'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'filmdatabase.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()

db = SQLAlchemy(app)
Migrate(app,db)

from mijn_project.Directors.view import Directors_blueprint
from mijn_project.Films.view import Films_blueprint
from mijn_project.Users.view import Users_blueprint
from mijn_project.Actors.view import Actors_blueprint

app.register_blueprint(Directors_blueprint,url_prefix="/directors")
app.register_blueprint(Films_blueprint,url_prefix='/films')
app.register_blueprint(Users_blueprint,url_prefix='/users')
app.register_blueprint(Actors_blueprint,url_prefix='/actors')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "Users.login"


from mijn_project.models import Users

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

