from src.entity.todo_list import TodoList
from .model import Listmodel


def convert_entity_to_model(entity: TodoList):
    lm = Listmodel(id=entity.id,title=entity.title,description=entity.description)
    return lm

def convert_model_to_entity(model: Listmodel):
    list_entity = TodoList(_id=model.id,title=model.title,todo_items=model.item,description=model.description)
    return list_entity
