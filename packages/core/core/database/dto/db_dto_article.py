from dataclasses import dataclass
from datetime import datetime

from core.constants.record_status import RecordStatus


@dataclass(frozen=True)
class DbDtoArticle:
    id: str
    title: str
    slug: str
    description: str
    body: str
    userId: str
    statusId: RecordStatus
    createdAt: datetime
    updatedAt: datetime
