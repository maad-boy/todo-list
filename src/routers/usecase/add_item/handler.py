from flask import Request

from src.entity import TodoItem
from src.routers.base_handler import BaseHandler, BaseRequest, BaseResponse
from src.routers.usecase.add_item.request import AddItemRequest
from .response import AddItemResponse
from src.service import get_list_service



class AddItemHandler(BaseHandler):
    def get_request(self, req: Request) -> BaseRequest:
        return AddItemRequest(req)

    def handle_request(self, req: AddItemRequest) -> AddItemResponse:
        _todo_item = TodoItem(list_id=req.list_id,description=req.description)
        get_list_service().add_item(_todo_item)
        return AddItemResponse()


def get_handler():
    return AddItemHandler()