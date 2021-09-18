from app import create_app, db

if __name__ == '__main__':
    flask_app = create_app("dev")
    #create database with app_context (i.e. relevant for the running app configuration)
    with flask_app.app_context():
        db.create_all()
    #run the app
    flask_app.run()

