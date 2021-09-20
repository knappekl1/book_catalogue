#app/auth/routes.py


from flask import render_template, flash, redirect, url_for
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.auth.models import User
from flask_login import login_user, logout_user, login_required, current_user


@at.route('/register', methods=['GET', 'POST'])
def register_user():
    #if user logged in => exit function
    if current_user.is_authenticated:
        flash("Already logged-in")
        return redirect(url_for("main.display_books"))
    form = RegistrationForm()
    
    #POST request.method path
    if form.validate_on_submit(): #combines if post and validation of the form 
        User.create_user(
            user=form.name.data,
            email=form.mail.data,
            password=form.password.data)
        flash('Registration Successful')
        return redirect(url_for('authentication.do_the_login'))

    #GET request.method path
    return render_template('registration.html', form=form)


@at.route('/login', methods=['GET', 'POST'])
def do_the_login():
    
    if current_user.is_authenticated:
        flash("Already logged-in")
        return redirect(url_for("main.display_books"))

    form = LoginForm()

    #POST request.method path
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.mail.data).first()

        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials, Please try again')
            return redirect(url_for('authentication.do_the_login'))

        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('main.display_books'))
    #GET request.method path
    return render_template('login.html', form=form)

@at.route("/logout", methods=["GET","POST"])
@login_required
def do_the_logout():
    logout_user()
    return redirect(url_for("main.display_books"))

@at.app_errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404