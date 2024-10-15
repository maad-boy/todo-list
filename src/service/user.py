from typing import List

from src.entity import User
from .repos import get_user_repo, UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo):
        self._user_repo: UserRepo = user_repo

    def create_user(self, user: User):
        return self._user_repo.create_user(user)

    def get_all_users(self) -> List[User]:
        users = self._user_repo.get_all_users()
        return users

def get_user_service() -> UserService:
    return UserService(get_user_repo())
