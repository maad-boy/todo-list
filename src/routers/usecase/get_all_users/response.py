from typing import List

from src.entity import User
from src.routers.base_handler import BaseResponse

class GetAllUsersResponse(BaseResponse):
    def __init__(self, users: List[User]):
        self._users = users

    @staticmethod
    def _get_user_json(user: User) -> dict:
        data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
        }
        return data

    def to_json(self) -> dict:
        return {"users": [self._get_user_json(user) for user in self._users]}