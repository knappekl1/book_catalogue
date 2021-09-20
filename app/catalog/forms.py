#app/catalog/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField, BooleanField, IntegerField, FloatField, SelectField
#from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from wtforms import validators as val
from app.catalog.models import Book, Publication

class EditBookForm(FlaskForm):
    title=StringField("Book Title", validators=[val.DataRequired()])
    author=StringField("Book Author", validators=[val.DataRequired()])
    format=StringField("Book Format", validators=[val.DataRequired()])
    num_pages=StringField("No. of Pages", validators=[val.DataRequired()])
    submit=SubmitField("Update")

class CreateBookForm(FlaskForm):
    title=StringField("Book Title", validators=[val.DataRequired()])
    author=StringField("Book Author", validators=[val.DataRequired()])
    avg_rating = FloatField("Rating", validators=[val.DataRequired()])
    format=SelectField("Book Format", validators=[val.DataRequired()], choices=["Hardcover","MassMarket Paperback","Paperback","ePub"])
    num_pages=IntegerField("No. of Pages", validators=[val.DataRequired()])
    image = StringField("Image URL", validators=[val.DataRequired()]) #val.url(require_tld=False, message="Invalid URL")]
    pub_id = IntegerField("Publisher ID", validators=[val.DataRequired()])
    submit=SubmitField("Create")