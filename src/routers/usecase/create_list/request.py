import flask
from src.routers.base_handler import BaseRequest


class CreateListRequest(BaseRequest):
    def __init__(self, req: flask.Request):
        self._req = req
        if req is  None:
            return
        data = req.get_json()
        self.title = data.get("title", "")
        self.description = data.get("description", "")


    def is_valid(self):
        if self.title == "" or self._req is None or self.description == "":
            return False
        return True

