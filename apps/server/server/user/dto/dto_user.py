from dataclasses import dataclass
from typing import Optional

from core.database.dto.db_dto_user import DbDtoUser
from server.utils.json_web_token import sign_json_web_token


@dataclass
class DtoUser:

    username: str
    email: str
    bio: Optional[str]
    image: Optional[str]
    token: Optional[str]

    def __init__(
        self,
        db_dto_user: DbDtoUser
    ):
        self.username = db_dto_user.username
        self.email = db_dto_user.email
        self.bio = db_dto_user.bio
        self.image = db_dto_user.image
        self.token = self.get_access_token(db_dto_user)

    def get_access_token(self, db_dto_user: DbDtoUser) -> str:
        token = sign_json_web_token(db_dto_user=db_dto_user)
        return token
