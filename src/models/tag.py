from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tag:
    tag_id: str
    name: str          # e.g. urgent, backend, blocker
    created_at: datetime
