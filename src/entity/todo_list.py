import uuid
from typing import List
from .todo_item import TodoItem
from src.enums import TodoItemStatus
from typing import Optional


class TodoList:
    def __init__(self, title: str, description: str, _id: Optional[int] = None, todo_items=None):
        self.id = _id if not None else uuid.uuid4().int % (1 << 16)
        self.title = title
        self.items = todo_items if not None else List[
            TodoItem(description="default", list_id=_id, status=TodoItemStatus.PENDING)]
        self.description = description
