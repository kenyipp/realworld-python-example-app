from typing import Optional

from core.database.dto.db_dto_user import DbDtoUser


class DtoProfile:

    username: str
    email: str
    bio: Optional[str]
    image: Optional[str]
    following: bool

    def __init__(
        self,
        db_dto_user: DbDtoUser,
        following: bool
    ):
        self.username = db_dto_user.username
        self.email = db_dto_user.email
        self.bio = db_dto_user.bio
        self.image = db_dto_user.image
        self.following = following
