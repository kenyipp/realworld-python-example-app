from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UserFollow(Base):
    __tablename__ = "user_follow"

    id = Column("article_id", String, primary_key=True)
    follower_id = Column("follower_id", String)
    following_id = Column("following_id", String)
    record_status = Column("record_status", String)
    created_at = Column("created_at", DateTime)
    updated_at = Column("updated_at", DateTime)

    def __init__(
        self,
        id: str,
        follower_id: str,
        following_id: str,
        record_status: str,
        created_at: DateTime,
        updated_at: DateTime,
    ) -> None:
        self.id = id
        self.follower_id = follower_id
        self.following_id = following_id
        self.record_status = record_status
        self.created_at = created_at
        self.updated_at = updated_at
