from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

load_dotenv()
TMDB_API_KEY = os.environ.get("TMDB_API_KEY")
SEARCH_MOVIE_URL = "https://api.themoviedb.org/3/search/movie"
DETAIL_MOVIE_URL = "https://api.themoviedb.org/3/movie"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"


def get_movies(search: str) -> list:
    params = {
        "api_key": TMDB_API_KEY,
        "query": search
    }
    response = requests.get(url=SEARCH_MOVIE_URL, params=params)
    response.raise_for_status()

    data = response.json()
    return data["results"]


def get_movie_detail(movie_id: int) -> dict:
    params = {
        "api_key": TMDB_API_KEY,
    }
    response = requests.get(url=f"{DETAIL_MOVIE_URL}/{movie_id}", params=params)
    response.raise_for_status()

    data = response.json()
    return {
        "title": data["title"],
        "img_url": f"{IMAGE_URL}{data['poster_path']}",
        "year": int(data["release_date"].split("-")[0]),
        "description": data["overview"]
    }


class EditForm(FlaskForm):
    rating = FloatField('Your Rating Out Of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review')
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.sqlite"
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(120))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(120))
    img_url = db.Column(db.String(250))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id: int):
    edit_form = EditForm()
    requested_movie = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        requested_movie.rating = float(edit_form.rating.data)
        if edit_form.review.data:
            requested_movie.review = edit_form.review.data

        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=requested_movie, form=edit_form)


@app.route("/delete-movie/<int:movie_id>")
def delete_movie(movie_id: int):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        searched_movies = get_movies(add_form.title.data)
        return render_template("select.html", movies=searched_movies)
    return render_template("add.html", form=add_form)


@app.route("/add-movie/<int:movie_id>")
def add_movie(movie_id: int):
    movie = get_movie_detail(movie_id)
    new_movie = Movie(title=movie["title"],
                      img_url=movie["img_url"],
                      description=movie["description"],
                      year=movie["year"])
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', movie_id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
