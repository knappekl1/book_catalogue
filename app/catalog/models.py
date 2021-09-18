#/catalog/models.py

#import db instance from app package (instantiated in app/__init__.py file)
from app import db
from datetime import datetime

#create model
class Publication(db.Model):
    __tablename__="publication"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return f"The publisher name is:{self.name}"


class Book(db.Model):
    '''
    avg_rating = rating, float
    format = publishing format (ebook, hardcover, paperback), str
    image = link to book image, str 
    num_pages = number of pages, int
    pub_id = id of the publisher, int
    '''
    __tablename__="book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())
    #relationship
    pub_id = db.Column(db.Integer, db.ForeignKey("publication.id"))

    def __init__(self, title,author, avg_rating, format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id
    
    def __repr__(self):
        return f"{self.title} by {self.author}"
