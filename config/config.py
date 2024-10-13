from .service import Service

class Config:
    def __init__(self, service: dict):
        self.service: Service = Service(**service)

