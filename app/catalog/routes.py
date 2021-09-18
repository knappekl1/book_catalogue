
import re
from app.catalog import main
from app import db
#(since Model is in same package/folder/ from models import ... would suffice)
from app.catalog.models import Publication, Book 
from flask import render_template

@main.route("/")
@main.route("/home")
def display_books():
    books = db.session.query(Book, Publication).join(Publication).all()
    return render_template("home.html",books=books)

@main.route("/display/publisher/<publ_id>")
def display_publisher(publ_id):
    publisher = Publication.query.filter_by(id=publ_id).first()
    pub_books = Book.query.filter_by(pub_id = publ_id).all()

    return render_template("publisher.html", publisher = publisher, books = pub_books)