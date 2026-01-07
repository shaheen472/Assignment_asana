from dataclasses import dataclass
from datetime import datetime


@dataclass
class TeamMembership:
    user_id: str
    team_id: str
    joined_at: datetime
    is_admin: bool
