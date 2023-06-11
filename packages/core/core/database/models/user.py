from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column("user_id", String, primary_key=True)
    username = Column("username", String)
    email = Column("email", String)
    bio = Column("bio", String)
    image = Column("image", String)
    password_salt = Column("password_salt", String)
    password_hash = Column("password_hash", String)
    record_status = Column("record_status", String)
    created_at = Column("created_at", DateTime)
    updated_at = Column("updated_at", DateTime)

    def __init__(
        self, id, username, email, bio, image, password_salt, password_hash
    ):
        self.id = id
        self.username = username
        self.email = email
        self.bio = bio
        self.image = image
        self.password_salt = password_salt
        self.password_hash = password_hash
        self.record_status = "normal"
