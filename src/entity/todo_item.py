
from src.enums import TodoItemStatus

class TodoItem:
    def __init__(self, _id: str, description: str, status: TodoItemStatus):
        self.id: str = _id
        self.description: str = description
        self.status: TodoItemStatus = status
