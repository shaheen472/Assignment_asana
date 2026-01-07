from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Project:
    project_id: str
    team_id: str
    org_id: str
    name: str
    description: str
    status: str
    start_date: date
    end_date: date
    created_at: datetime
