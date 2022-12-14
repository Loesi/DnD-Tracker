from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "asdfasdgdsrf"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    #Alle Klassen importieren
    from .models import Encounter, Entity

    create_database(app)

    return app

def create_database(app):
    if not path.exists(f"instance/{DB_NAME}"):
        with app.app_context():
            db.create_all()
        print("Database created!")