from mijn_project import db
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, LoginManager





class Directors(db.Model):
    __tablename__ = 'Directors'

    director_id = db.Column(db.Integer,primary_key= True)
    director_name = db.Column(db.Text)
    director_description = db.Column(db.Text)
    director_picture = db.Column(db.Text)
    director_date = db.Column(db.Text)
    director_film_ID = db.relationship('Films',backref='Directors',lazy='dynamic')



    def __init__(self, director_name, director_description, director_picture, director_date):
        self.director_name = director_name
        self.director_description = director_description
        self.director_picture = director_picture
        self.director_date = director_date

    def __repr__(self):
        return f"{self.director_name} {self.director_description}"

    #def picture(self):
     #   return f"{self.director_name}"










class Films(db.Model):

    __tablename__ = 'Films'

    film_id = db.Column(db.Integer,primary_key= True)
    film_name = db.Column(db.Text)
    film_length = db.Column(db.Integer)
    film_rating = db.Column(db.Integer)
    film_year = db.Column(db.Integer)
    film_genre = db.Column(db.Text)
    film_director = db.Column(db.Integer,db.ForeignKey('Directors.director_id'))
    film_trailer = db.Column(db.Text)
    film_foto = db.Column(db.Text)
    film_description = db.Column(db.Text)
    film_summary = db.Column(db.Text)
    film_roles = db.relationship('Roles',backref='Films',lazy='dynamic')




    def __init__(self, film_name, film_length, film_rating, film_year, film_genre, film_director, film_trailer, film_foto, film_description, film_summary):
        self.film_name = film_name
        self.film_length = film_length
        self.film_rating = film_rating
        self.film_year = film_year
        self.film_genre = film_genre
        self.film_director = film_director
        self.film_trailer = film_trailer
        self.film_foto = film_foto
        self.film_description = film_description
        self.film_summary = film_summary



    def __repr__(self):
        return f"Deze student heet {self.film_name}"









class Users(db.Model, UserMixin):
    __tablename__ = 'Users'

    user_id = db.Column(db.Integer,primary_key= True)
    user_name = db.Column(db.Text)
    user_email = db.Column(db.Text)
    user_password = db.Column(db.Text)
    user_role = db.Column(db.Text)



    def __init__(self, user_name, user_email, user_password, user_role):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = generate_password_hash(user_password)
        self.user_role = user_role

    def check_password(self, user_password):
        return check_password_hash(self.user_password, user_password)

    def get_id(self):
        return (self.user_id)


class Roles(db.Model, UserMixin):
    __tablename__ = 'Roles'

    role_id = db.Column(db.Integer,primary_key= True)
    role = db.Column(db.Text)
    role_film = db.Column(db.Integer, db.ForeignKey('Films.film_id'))
    role_actor = db.Column(db.Integer, db.ForeignKey('Actors.actor_id'))



    def __init__(self, role, role_filmid, role_actorid):
        self.role = role
        self.role_filmid = role_filmid
        self.role_actorid = role_actorid


class Actors(db.Model, UserMixin):
    __tablename__ = 'Actors'

    actor_id = db.Column(db.Integer,primary_key= True)
    actor_name = db.Column(db.Text)
    actor_picture = db.Column(db.Text)
    actor_role = db.relationship('Roles',backref='Actors',lazy='dynamic')



    def __init__(self, actor_name, actor_picture):
        self.actor_name = actor_name
        self.actor_picture = actor_picture
