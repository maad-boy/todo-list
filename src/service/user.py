from src.entity import User
from .repos import get_user_repo, UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo):
        self._user_repo: UserRepo = user_repo

    def create_user(self, user: User):
        return self._user_repo.create_user(user)

def get_user_service() -> UserService:
    return UserService(get_user_repo())
