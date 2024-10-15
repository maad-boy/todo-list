from typing import List

from src.entity import User
from src.database.sql_alchamy import db
from .transformation import convert_entity_to_model, convert_model_to_entity
from flask_sqlalchemy import SQLAlchemy

class UserRepo:
    def __init__(self, client: SQLAlchemy):
        self._convert_entity_to_model = convert_entity_to_model
        self._convert_model_to_entity = convert_model_to_entity
        self._client: client = client

    def create_user(self, user: User):
        db_model = self._convert_entity_to_model(user)
        self._client.session.add(db_model)
        self._client.session.commit()

    def get_all_users(self) -> List[User]:
        db_models = self._client.session.query(User).all()
        users = [self._convert_model_to_entity(model) for model in db_models]
        return users


def get_user_repo() -> UserRepo:
    return UserRepo(client=db)

