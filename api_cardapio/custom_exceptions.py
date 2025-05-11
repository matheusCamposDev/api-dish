class UserAlreadyExistsException(Exception):
    pass


class InvalidUserDataException(Exception):
    pass


class DatabaseException(Exception):
    pass


class Unauthorized(Exception):
    pass
