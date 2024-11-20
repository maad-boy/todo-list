import flask
from flask import Request

from src.routers.base_handler import BaseHandler, BaseResponse, BaseRequest
from src.entity import User
from src.service import get_user_service

from .request import GetUserByIdRequest

class GetUserByIdHandler(BaseHandler):
    def get_request(self, req: Request) -> BaseRequest:
        return GetUserByIdRequest(req)

    def handle_request(self, req: BaseRequest) -> BaseResponse:
        user_id =
        user = get_user_service().get_user_by_id(req)