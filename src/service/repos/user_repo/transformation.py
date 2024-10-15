from src.entity import User
from .model import UserModel

def convert_entity_to_model(entity: User) -> UserModel:
    um = UserModel(id=entity.id, username=entity.name, email=entity.email, password=entity.password)
    return um

def convert_model_to_entity(model: UserModel) -> User:
    user = User(_id=model.id, name=model.username,  email=model.email, password=model.password)
    return user


