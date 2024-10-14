from flask import request

class BaseRequest:
    def __init__(self, req: request):
        pass

    def is_valid(self):
        pass
