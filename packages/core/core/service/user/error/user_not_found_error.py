class UserNotFoundError(Exception):

    def __init__(self):
        self.code = "USER_NOT_FOUND"
        self.message = "Sorry, we could not find an user with that information. Please try again with a different email or username"
