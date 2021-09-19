from app.auth import authentication as at
from flask import render_template, request
from app.auth.forms import RegistrationForm

@at.route("/register", methods=["GET","POST"])
def register_user():
    name=None
    mail=None
    #Instantiate RegistrationForm class
    form = RegistrationForm()

    if request.method =="POST":
        name = form.name.data
        mail = form.mail.data
    
    return render_template("registration.html", form=form, name=name, mail=mail)

