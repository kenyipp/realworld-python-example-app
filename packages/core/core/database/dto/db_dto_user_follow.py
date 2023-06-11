from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserFollow:
    id: str
    follower_id: str
    following_id: str
    record_status: str
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_user_follow(row):
        return UserFollow(
            id=row.id,
            follower_id=row.follower_id,
            following_id=row.following_id,
            record_status=row.record_status,
            created_at=row.created_at,
            updated_at=row.updated_at
        )
