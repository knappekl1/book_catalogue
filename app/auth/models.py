#app/auth/models.py

from app import db, bcrypt
from datetime import datetime

class User(db.Model):
    __tablename__="user"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    user_email = db.Column(db.String(30), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)

    @classmethod
    def create_user(cls, user, email, password):
        
        user = cls(user_name=user, user_email=email, user_password=bcrypt.generate_password_hash(password).decode("UTF-8"))
        db.session.add(user)
        db.session.commit()
        return




