from dataclasses import dataclass
from datetime import datetime


@dataclass
class Team:
    team_id: str
    org_id: str
    name: str
    description: str
    created_at: datetime
