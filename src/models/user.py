from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    user_id: str
    org_id: str
    name: str
    email: str
    role: str
    job_title: str
    created_at: datetime
    is_active: bool
