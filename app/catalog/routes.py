
import re
from app.catalog import main
from app import db
#(since Model is in same package/folder/ from models import ... would suffice)
from app.catalog.models import Publication, Book 
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app.catalog.forms import EditBookForm

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

@main.route("/book/delete/<book_id>", methods=["POST","GET"])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)

    if request.method == "POST":
        db.session.delete(book)
        db.session.commit()
        flash("Book delete successful")
        return redirect(url_for("main.display_books"))
    
    return render_template("delete_book.html", book=book, book_id = book_id)

@main.route("/book/edit/<book_id>", methods=["POST","GET"])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBookForm(obj=book)

    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.format = form.format.data
        book.num_pages = form.pages.data

        db.session.add(book)
        db.session.commit()

        flash("Book edited sucessfully")

        return redirect(url_for("main.display_books"))
    
    return render_template("edit_book.html",form=form)
