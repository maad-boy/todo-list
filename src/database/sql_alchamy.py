from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app: Flask) -> None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.data/database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
