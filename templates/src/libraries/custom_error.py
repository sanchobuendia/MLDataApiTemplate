class AlreadyExist(Exception):
    def __init__(self, message):
        self.message = message.replace("  ", "").replace("\n", "")
        super().__init__(self.message)


class NotFound(Exception):
    def __init__(self, message):
        self.message = message.replace("  ", "").replace("\n", "")
        super().__init__()

    def __str__(self):
        return self.message


class AuthenticationError(Exception):
    def __init__(self, message):
        self.message = message.replace("  ", "").replace("\n", "")
        super().__init__(self.message)


class InvalidPassword(Exception):
    pass


class AlreadyConnected(Exception):
    def __init__(self, message):
        self.message = message.replace("  ", "").replace("\n", "")
        super().__init__(self.message)


class Forbidden(Exception):
    pass
