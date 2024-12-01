from flask import Request

from src.routers.base_handler import BaseHandler, BaseResponse
from src.entity import TodoList
from src.service import get_list_service

from .request import CreateListRequest
from .response import CreateListResponse

class CreateListHandler(BaseHandler):
    def get_request(self, req: Request) -> CreateListRequest:
        return CreateListRequest(req)

    def handle_request(self, req: CreateListRequest) -> BaseResponse:
        _todo_list = TodoList(title=req.title, description=req.description)
        get_list_service().create_list(_todo_list)
        return CreateListResponse()

def get_handler():
    return CreateListHandler()
