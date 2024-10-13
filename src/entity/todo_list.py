from typing import List
from .todo_item import TodoItem

class TodoList:
    def __init__(self, _id: str, title: str, todo_items: List[TodoItem]):
        self.id = _id
        self.title = title
        self.list: List[TodoItem] = todo_items
