from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,SubmitField,PasswordField
#from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from wtforms import validators as val

class RegistrationForm(FlaskForm):
    
    name = StringField("Name", validators=[val.DataRequired(), val.Length(3,15, message="3 to 15 characters")])
    mail = StringField("Email", validators=[val.DataRequired(),val.Email()])
    password = PasswordField("Password", validators=[val.DataRequired(), val.Length(5), val.EqualTo("confirm", message="Passwords do not match")])
    confirm = PasswordField("Confirm", validators=[val.DataRequired()])
    submit = SubmitField("Register")
