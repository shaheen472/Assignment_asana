from dataclasses import dataclass
from datetime import datetime


@dataclass
class Organization:
    org_id: str
    name: str
    mail: str
    created_at: datetime
