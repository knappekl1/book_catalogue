from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField, BooleanField
#from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from wtforms import validators as val
from app.auth.models import User

#function is added to erlevant field in the Form class
def item_exists(form, field):
    if field.name == "mail":
        email = User.query.filter_by(user_email = field.data).first()
        if email:
            raise val.ValidationError("Email already exists")
    if field.name == "name":
        name = User.query.filter_by(user_name = field.data).first()
        if name:
            raise val.ValidationError("User already registered")


class RegistrationForm(FlaskForm):
    
    name = StringField("Name", validators=[val.DataRequired(), val.Length(3,15, message="3 to 15 characters")])
    #Custom validation email_exists added to the mail field of the Form class
    mail = StringField("Email", validators=[val.DataRequired(),val.Email(), item_exists])
    password = PasswordField("Password", validators=[val.DataRequired(), val.Length(5), val.EqualTo("confirm", message="Passwords do not match")])
    confirm = PasswordField("Confirm", validators=[val.DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    mail = StringField("Email", validators=[val.DataRequired(),val.Email()])
    password = PasswordField("Password", validators=[val.DataRequired(), val.Length(5)])
    stay_loggedin = BooleanField("Stay logged-in")
    submit = SubmitField("Log-In")