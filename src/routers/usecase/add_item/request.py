import flask
from src.routers.base_handler import BaseRequest


class AddItemRequest(BaseRequest):
    def __init__(self, res:flask.request):
        self._res = res
        if res is None:
            return
        data = res.get_json()
        self.list_id = data.get('list_id', "")
        self.description = data.get('description', "")

    def is_valid(self):
        pass
