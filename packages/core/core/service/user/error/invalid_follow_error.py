class InvalidFollowError(Exception):

    def __init__(self, message: str):
        self.code = "USER_INVALID_FOLLOW"
        self.message = message
