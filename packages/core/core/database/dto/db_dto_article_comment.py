from dataclasses import dataclass
from datetime import datetime

from core.constants.record_status import RecordStatus


@dataclass
class DbDtoArticleComment:
    id: str
    body: str
    user_id: str
    record_status: RecordStatus
    created_at: datetime
    updated_at: datetime
