from src.entity import User
from src.database.sql_alchamy import db
from .transformation import convert_entity_to_model
from flask_sqlalchemy import SQLAlchemy

class UserRepo:
    def __init__(self, client: SQLAlchemy):
        self._convert_entity_to_model = convert_entity_to_model
        self._client: client = client

    def create_user(self, user: User):
        db_model = self._convert_entity_to_model(user)
        self._client.session.add(db_model)
        self._client.session.commit()


def get_user_repo() -> UserRepo:
    return UserRepo(client=db)

