from dataclasses import dataclass
from datetime import datetime


@dataclass
class Comment:
    comment_id: str
    task_id: str
    user_id: str
    type: str          # e.g. "comment", "system"
    content: str
    created_at: datetime
