from src.entity import User
from .transformation import convert_entity_to_model

class UserRepo:
    def __init__(self):
        self._convert_entity_to_model = convert_entity_to_model

    def create_user(self, user: User):
        db_model = self._convert_entity_to_model(user)
        db_model.save()


def get_user_repo() -> UserRepo:
    return UserRepo()
