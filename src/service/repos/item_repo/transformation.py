from src.entity import TodoItem
from .model import Itemmodel



def convert_entity_to_model(entity: TodoItem):
    im = TodoItem(id=entity.id, list_id=entity.list_id,description=entity.description,status=entity.status)
    return im

def convert_model_to_entity(model: Listmodel):
    item_entity = TodoItem(id=model.id,description=model.description,list_id=model.list_id,status=model.status)
    return item_entity
