from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

# USE SQLITE
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books ("
#                "id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
    db = SQLAlchemy(app)

    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(120), unique=True, nullable=False)
        author = db.Column(db.String(120), nullable=False)
        rating = db.Column(db.Float, nullable=False)


    db.create_all()

    # CREATE RECORD
    # new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    # db.session.add(new_book)
    # db.session.commit()

    # READ ALL RECORDS
    # all_books = Book.query.all()

    # READ PARTICULAR BOOK BY QUERY
    # book = Book.query.filter_by(title="Harry Potter").first()
    # book = Book.query.get(1)

    # UPDATE PARTICULAR BOOK BY QUERY
    # book = Book.query.filter_by(title="Harry Potter").first()
    # book.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit()

    # DELETE
    # book = Book.query.get(1)
    # db.session.delete(book)
    # db.session.commit()


@app.route('/')
def home():
    with app.app_context():
        all_books = Book.query.all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('add'))
    return render_template('add.html')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get("id")
    with app.app_context():
        requested_book = Book.query.get(book_id)

    if request.method == "POST":
        with app.app_context():
            requested_book = Book.query.get(book_id)
            requested_book.rating = request.form["rating"]
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=requested_book)


if __name__ == "__main__":
    app.run(debug=True)

