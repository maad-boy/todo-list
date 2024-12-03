from flask_sqlalchemy import SQLAlchemy
from src.database.sql_alchamy import db

from src.entity import TodoList

from .transformation import convert_entity_to_model, convert_model_to_entity

class ListRepo:
    def __init__(self, client: SQLAlchemy):
        self._convert_entity_to_model = convert_entity_to_model
        self._convert_model_to_entity = convert_model_to_entity
        self._client: client = client

    def create_list(self, todo_list: TodoList):
        db_model = self._convert_entity_to_model(todo_list)
        self._client.session.add(db_model)
        self._client.session.commit()



def get_list_repo() -> ListRepo:
    return ListRepo(client=db)