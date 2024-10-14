from src.entity import User
from .model import UserModel

def convert_entity_to_model(entity: User) -> UserModel:
    um = UserModel(id=entity.id, username=entity.name, email=entity.email, password=entity.password)
