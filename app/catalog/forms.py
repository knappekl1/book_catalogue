from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField, BooleanField
#from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from wtforms import validators as val
from app.catalog.models import Book, Publication

class EditBookForm(FlaskForm):
    title=StringField("Book Title", validators=[val.DataRequired()])
    author=StringField("Book Author", validators=[val.DataRequired()])
    format=StringField("Book Format", validators=[val.DataRequired()])
    pages=StringField("No. of Pages", validators=[val.DataRequired()])
    submit=SubmitField("Update")