from src.routers.base_handler import BaseResponse

class CreateListResponse(BaseResponse):
    def to_json(self):
        return {}
