from src.routers.base_handler import BaseResponse
from src.entity import User

class GetUserByIdResponse(BaseResponse):
    def __init__(self, user: User):
        self._user = user

    def to_json(self) -> dict:
        return {"email": self._user.email, "id": self._user.id, "name": self._user.name}
