from src.entity import TodoList
from .repos import ListRepo, get_list_repo


class TodoListService:
    def __init__(self, list_repo:ListRepo):
        self._list_repo: ListRepo = list_repo

    def create_list(self, todo_list: TodoList):
        return self._list_repo.create_list(todo_list)


def get_list_service() -> TodoListService:
    return TodoListService(get_list_repo())