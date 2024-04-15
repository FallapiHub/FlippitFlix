from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, TextAreaField, PasswordField

class Voegfilm(FlaskForm):

    film_name = StringField('Film Name:')
    film_length = IntegerField('Film Length:')
    film_rating = IntegerField('Film Rating: ')
    film_year = IntegerField('Film Year:')
    film_genre = StringField('Film genre: ')
    film_director = IntegerField('Director: ')
    film_actor = StringField('Actor: ')
    film_trailer = StringField('youtube link dinges: ')
    film_foto = StringField('Foto link in verkenner: ')
    film_description = TextAreaField('Film description: ')
    submit = SubmitField('Add the movie')


class Voegdirector(FlaskForm):

    director_name = StringField('Director name: ')
    director_description = TextAreaField('Director description: ')
    director_picture = StringField('Director picture: ')
    director_date = StringField('Director date: ')
    submit = SubmitField('Add the director')


class Voeguser(FlaskForm):




    user_name = StringField('User name: ')
    user_email = EmailField("User email: ")
    user_password = PasswordField("Password: ")
    submit = SubmitField('Add user: ')