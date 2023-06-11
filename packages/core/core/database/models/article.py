from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Article(Base):
    __tablename__ = "article"

    id = Column("article_id", String, primary_key=True)
    title = Column("title", String)
    slug = Column("slug", String)
    description = Column("description", String)
    body = Column("body", String)
    user_id = Column("user_id", String)
    record_status = Column("record_status", String)
    created_at = Column("created_at", DateTime)
    updated_at = Column("updated_at", DateTime)

    def __init__(self, id: str, title: str, slug: str, description: str, body: str,
                 userId: str, statusId: str) -> None:
        self.id = id
        self.title = title
        self.slug = slug
        self.description = description
        self.body = body
        self.userId = userId
        self.statusId = statusId
