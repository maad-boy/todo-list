from flask import request

from .request import BaseRequest
from .response import BaseResponse


class BaseHandler:
    def get_request(self, req: request) -> BaseRequest:
        pass

    def handle_request(self, req: BaseRequest) -> BaseResponse:
        pass
