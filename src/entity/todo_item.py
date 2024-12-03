import uuid
from typing import Optional

from src.enums import TodoItemStatus

class TodoItem:
    def __init__(self, description: str, list_id: int, id: Optional[int]=None, status=None):
        self.id = id if not None else uuid.uuid4().int % (1 << 16)
        self.description: str = description
        self.status: TodoItemStatus = status if not None else TodoItemStatus.PENDING
        self.list_id = list_id

