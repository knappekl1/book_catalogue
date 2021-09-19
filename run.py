from app import create_app, db
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app("dev")
    #create database with app_context (i.e. relevant for the running app configuration)
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry', email='harry@hogwarts.com', password='secret')
    #run the app
    flask_app.run()

