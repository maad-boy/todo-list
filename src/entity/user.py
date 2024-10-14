import uuid


class User:
    def __init__(self, name, email, password):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.password = password
