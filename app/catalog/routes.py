#app/catalog/routes.py

from app.catalog import main
from app import db
#(since Model is in same package/folder/ from models import ... would suffice)
from app.catalog.models import Publication, Book 
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app.catalog.forms import EditBookForm, CreateBookForm

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
    form = EditBookForm(obj=book) #obj=book statement feeds the form from model (i.e. database table) for the instance to show values from db in form, form field names must be same as model class properties names to work.

    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.format = form.format.data
        book.num_pages = form.num_pages.data

        db.session.add(book)
        db.session.commit()

        flash("Book edited sucessfully")

        return redirect(url_for("main.display_books"))
    
    return render_template("edit_book.html",form=form)

@main.route("/create_book/<pub_id>", methods=["GET","POST"])
@login_required
def create_book(pub_id):
    form = CreateBookForm()
    form.pub_id.data = pub_id
    
    if form.validate_on_submit():
        if not Book.query.filter_by(title=form.author.data, author=form.author.data).first():
            book = Book(form.title.data, form.author.data, form.avg_rating.data, form.format.data, form.image.data, form.num_pages.data, 
                        form.pub_id.data)
            db.session.add(book)
            db.session.commit()
            flash("Book record created")
            return redirect(url_for("main.display_books"))
        else:
            flash("Book already exists in database")
    return render_template("create_book.html", form=form)

