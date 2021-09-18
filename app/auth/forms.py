from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class RegistrationForm(FlaskForm):
    
    name = StringField("Your Name")
    mail = StringField("Email")
    submit = SubmitField("Register")