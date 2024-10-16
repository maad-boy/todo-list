import uuid
from typing import Optional


class User:
    def __init__(self, name, email, password, _id: Optional[int]=None):
        self.id: int = _id if not None else uuid.uuid4().int % (1 << 16)
        self.name = name
        self.email = email
        self.password = password
