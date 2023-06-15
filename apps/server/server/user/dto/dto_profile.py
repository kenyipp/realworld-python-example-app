from typing import Optional
from core.database.dto.db_dto_user import DbDtoUser

class DtoProfile:
    def __init__(
        self,
        db_dto_user: DbDtoUser,
        following: bool
    ):
        self.username: str = db_dto_user.username
        self.email: str = db_dto_user.email
        self.bio: Optional[str] = db_dto_user.bio
        self.image: Optional[str] = db_dto_user.image
        self.following: bool = following
