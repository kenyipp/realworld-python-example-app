class UserExistError(Exception):

    def __init__(self):
        self.code = "USER_EXISTED"
        self.message = "The provided email or username is already registered. \
            Please use a different email or username.",
