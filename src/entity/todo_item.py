import uuid
from typing import Optional

from src.enums import TodoItemStatus

class TodoItem:
    def __init__(self, description: str, status: TodoItemStatus, list_id: int, _id: Optional[int]=None):
        self.id = _id if not None else uuid.uuid4().int % (1 << 16)
        self.description: str = description
        self.status: TodoItemStatus = status
        self.list_id = list_id
