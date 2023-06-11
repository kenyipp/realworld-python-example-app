from dataclasses import dataclass


@dataclass
class DbDtoArticleMeta:
    id: str
    favorited: bool
    favorites_count: int
    following: bool
