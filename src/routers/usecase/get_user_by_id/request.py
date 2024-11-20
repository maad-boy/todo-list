import flask
from src.routers.base_handler import BaseRequest

class GetUserByIdRequest(BaseRequest):
    def __init__(self, req: flask.Request):
        self._req = req
        if req is None:
            return
        data = req.get_json()
        self.user_id = data.get("user_id", "")

    def is_valid(self):
        if isinstance(self.user_id, int):
           return True
        return False