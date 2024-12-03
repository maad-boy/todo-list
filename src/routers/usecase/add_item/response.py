from src.routers.base_handler import BaseResponse

class AddItemResponse(BaseResponse):
    def to_json(self):
        return {}
