from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from core.constants.record_status import RecordStatus
from core.database.models.user import User


@dataclass
class DbDtoUser:
    id: str
    username: str
    email: str
    bio: Optional[str]
    image: Optional[str]
    password_hash: str
    record_status: RecordStatus
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_user_model(row: User):
        return DbDtoUser(
            id=row.id,
            username=row.username,
            email=row.email,
            bio=row.bio,
            image=row.image,
            password_hash=row.password_hash,
            record_status=RecordStatus(row.record_status),
            created_at=row.created_at,
            updated_at=row.updated_at,
        )
