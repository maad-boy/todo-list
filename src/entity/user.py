import uuid
from typing import Optional


class User:
    def __init__(self, name, email, password, _id=Optional[int]):
        if _id is None:
            _id: int = uuid.uuid4().int % (1 << 16)
        self.id = _id
        self.name = name
        self.email = email
        self.password = password
