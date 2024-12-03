from flask_sqlalchemy import SQLAlchemy
from src.database.sql_alchamy import db
from .transformation import convert_entity_to_model, convert_model_to_entity
from src.entity import TodoItem

class ItemRepo:
    def __init__(self, client: SQLAlchemy):
        self._convert_entity_to_model = convert_entity_to_model
        self._convert_model_to_entity = convert_model_to_entity
        self._client: client = client

    def add_item(self, todo_item: TodoItem):
        db_model = self._convert_entity_to_model(todo_item)
        self._client.session.add(db_model)
        self._client.session.commit()


def get_item_repo():
    return ItemRepo(client=db)