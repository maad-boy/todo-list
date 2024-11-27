from flask import Request

from src.routers.base_handler import BaseHandler, BaseResponse, BaseRequest
from src.entity import User
from src.service import get_user_service
from .response import GetUserByIdResponse
from .request import GetUserByIdRequest

class GetUserByIdHandler(BaseHandler):
    def get_request(self, req: Request) -> BaseRequest:
        return GetUserByIdRequest(req)

    def handle_request(self, req: GetUserByIdRequest) -> BaseResponse:
        ID = req.user_id
        user = get_user_service().get_user_by_id(ID)
        return GetUserByIdResponse(user)


def get_handler() -> BaseHandler:
    return GetUserByIdHandler()