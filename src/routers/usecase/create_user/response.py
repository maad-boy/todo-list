from src.routers.base_handler import BaseResponse

class Response(BaseResponse):
    def to_json(self):
        return {}
