from dataclasses import dataclass
from typing import List


@dataclass
class DbDtoArticleTag:
    article_id: str
    tags: List[str]
