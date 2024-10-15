from flask import Request

from src.routers.base_handler import BaseHandler, BaseResponse
from src.service import get_user_service
from .request import GetAllUsersRequest
from .response import GetAllUsersResponse


class GetAllUsersHandler(BaseHandler):
    def get_request(self, req: Request) -> GetAllUsersRequest:
        return GetAllUsersRequest()

    def handle_request(self, req: GetAllUsersRequest) -> BaseResponse:
        users = get_user_service().get_all_users()
        return GetAllUsersResponse(users=users)


def get_handler() -> BaseHandler:
    return GetAllUsersHandler()
