
class LogInRequest:
    username: str
    password: str

    def __init__(self, request: dict):
        self.username = request['username']
        self.password = request['password']
