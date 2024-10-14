from flask import request
from src.routers.base_handler import BaseRequest

class Request(BaseRequest):
    def __init__(self, req: request):
        self._req = req
        if req is None:
            return
        data = req.get_json()
        self.email: str = data.get("email", "")
        self.password: str = data.get("password", "")
        self.name: str = data.get("name", "")

    def is_valid(self) -> bool:
        if self._req is None:
            return False
        if self.name == "" or self.email == "" or self.password == "":
            return False
        return True
