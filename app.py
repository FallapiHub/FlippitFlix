from flask import Flask, render_template, redirect, url_for, request, flash, session
from .__init__ import app, db
from .forms import Voegfilm, Voegdirector, Voeguser
from flask_migrate import Migrate


app.app_context().push()


migrate = Migrate(app, db)
from .models import Films, Directors, Users



@app.route('/')
def index():  # put application's code here
    #all = Directors.query.all()
    directors = db.session.query(Directors.director_name)
    director_pics = db.session.query(Directors.director_picture)
    director_ids = db.session.query(Directors.director_id)
    return render_template("home.html", directors=directors, director_pics=director_pics, director_ids=director_ids)

@app.route('/add/director', methods=['GET', 'POST'])
def add_director():
    form = Voegdirector()

    if form.validate_on_submit():
        director_name = form.director_name.data
        director_description = form.director_description.data
        director_picture = form.director_picture.data
        director_date = form.director_date.data

        # Voeg een nieuwe cursist toe aan de database
        new_director = Directors(director_name, director_description, director_picture, director_date)
        db.session.add(new_director)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_director.html', form=form)


@app.route('/add/film', methods=['GET', 'POST'])
def add_film():
    form = Voegfilm()

    if form.validate_on_submit():
        film_name = form.film_name.data
        film_length = form.film_length.data
        film_rating = form.film_rating.data
        film_year = form.film_year.data
        film_genre = form.film_genre.data
        film_director = form.film_director.data
        film_actor = form.film_actor.data
        film_trailer = form.film_trailer.data
        film_foto = form.film_foto.data
        film_description = form.film_description.data

        # Voeg een nieuwe cursist toe aan de database
        new_film = Films(film_name, film_length, film_rating, film_year, film_genre, film_director, film_actor, film_trailer, film_foto, film_description)
        db.session.add(new_film)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_film.html', form=form)


@app.route('/films')
def all_films():  # put application's code here
    #all = Directors.query.all()
    film_names = db.session.query(Films.film_name)
    film_ids = db.session.query(Films.film_id)
    film_pics = db.session.query(Films.film_foto)
    film_descriptions = db.session.query(Films.film_description)

    return render_template("all_films.html", film_names=film_names, film_ids=film_ids, film_pics=film_pics, film_descriptions=film_descriptions)

@app.route('/films/<film_page>', methods=['GET', 'POST'])
def view_film(film_page):  # put application's code here
    #all = Directors.query.all()
    film_id = film_page
    film_name = db.session.query(Films.film_name).filter_by(film_id=film_id).all()
    film_length = db.session.query(Films.film_length).filter_by(film_id=film_id).all()
    film_rating = db.session.query(Films.film_rating).filter_by(film_id=film_id).all()
    film_year = db.session.query(Films.film_year).filter_by(film_id=film_id).all()
    film_genre = db.session.query(Films.film_genre).filter_by(film_id =film_id).all()
    film_director = db.session.query(Films.film_director).filter_by(film_id=film_id).all()
    film_actor = db.session.query(Films.film_actor).filter_by(film_id=film_id).all()
    film_trailer = db.session.query(Films.film_trailer).filter_by(film_id=film_id).all()
    film_foto = db.session.query(Films.film_foto).filter_by(film_id=film_id).all()
    film_description = db.session.query(Films.film_description).filter_by(film_id=film_id).all()
    #director_name = db.session.query(Directors.director_name).filter_by(director_id=film_director).all()
    director_name = db.session.query(Directors.director_name).all()



    return render_template("view_film.html", film_name=film_name, film_length=film_length, film_rating=film_rating,film_year=film_year, film_genre=film_genre, film_director=film_director, film_actor=film_actor, film_trailer=film_trailer, film_foto=film_foto, film_description=film_description, director_name=director_name)




@app.route('/signup', methods=['GET', 'POST'])
def add_user():
    form = Voeguser()

    if form.validate_on_submit():
        user_name = form.user_name.data
        user_email = form.user_email.data
        user_password = form.user_password.data
        user_role = "user"

        # Voeg een nieuwe cursist toe aan de database
        new_user = Users(user_name, user_email, user_password, user_role)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_user.html', form=form)





@app.route('/directors/<director_page>', methods=['GET', 'POST'])
def view_director(director_page):  # put application's code here
    #all = Directors.query.all()
    director_id = director_page

    director_name = db.session.query(Directors.director_name).filter_by(director_id=director_id).all()
    director_date = db.session.query(Directors.director_date).filter_by(director_id=director_id).all()
    director_picture = db.session.query(Directors.director_picture).filter_by(director_id=director_id).all()
    director_description = db.session.query(Directors.director_description).filter_by(director_id=director_id).all()


    film_ids = db.session.query(Films.film_id).filter_by(film_director=director_id).all()
    #film_names = db.session.query(Films.film_name).filter_by(film_director=director_id).all()
    #film_pictures = db.session.query(Films.film_foto).filter_by(film_director=director_id).all()
    #film_descriptions = db.session.query(Films.film_description).filter_by(film_director=director_id).all()
    film_names = db.session.query(Films.film_name).all()
    film_pictures = db.session.query(Films.film_foto).all()
    film_descriptions = db.session.query(Films.film_description).all()


    return render_template("view_director.html", film_ids=film_ids, film_names=film_names, film_pictures=film_pictures, film_descriptions=film_descriptions, director_name=director_name, director_date=director_date, director_picture=director_picture, director_description=director_description, director_id=director_id)






if __name__ == '__main__':
    app.run()
