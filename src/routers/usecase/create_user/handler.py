from flask import request

from src.routers.base_handler import BaseHandler, BaseResponse
from src.entity import User
from src.service import get_user_service

from .request import Request
from .response import Response


class Handler(BaseHandler):
    def get_request(self, req: request) -> Request:
        return Request(req)

    def handle_request(self, req: Request) -> BaseResponse:
        user = User(name=req.name, email=req.email, password=req.password)
        get_user_service().create_user(user)
        return Response()

def get_handler() -> Handler:
    return Handler()

