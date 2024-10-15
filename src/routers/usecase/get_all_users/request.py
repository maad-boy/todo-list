from src.routers.base_handler import BaseRequest

class GetAllUsersRequest(BaseRequest):
    def is_valid(self):
        return True
