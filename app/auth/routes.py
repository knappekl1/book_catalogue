#app/auth/routes.py

from app.auth import authentication as at
from flask import render_template, request, flash, redirect, url_for
from app.auth.forms import RegistrationForm
from app.auth.models import User

@at.route("/register", methods=["GET","POST"])
def register_user():
    #Instantiate RegistrationForm class
    form = RegistrationForm()
    
    #POST request
    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.mail.data,
            password=form.password.data
        )
        
        flash("Registration Successful")
        return redirect(url_for("at.login_user")) #at is name of the blueprint authentication as imported above

    return render_template("registration.html", form=form)

@at.route("/login", methods=["GET","POST"])
def login_user():
    return render_template("login.html")

