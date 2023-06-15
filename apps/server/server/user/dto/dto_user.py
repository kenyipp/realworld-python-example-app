from typing import Optional
from core.database.dto.db_dto_user import DbDtoUser
from server.utils.json_web_token import sign_json_web_token

class DtoUser:
    def __init__(
        self,
        db_dto_user: DbDtoUser
    ):
        self.username: str = db_dto_user.username
        self.email: str = db_dto_user.email
        self.bio: Optional[str] = db_dto_user.bio
        self.image: Optional[str] = db_dto_user.image
        self.token: Optional[str] = self.get_access_token(db_dto_user)

    def get_access_token(db_dto_user: DbDtoUser) -> str:
        token = sign_json_web_token(db_dto_user=db_dto_user)
        return token
