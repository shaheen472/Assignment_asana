from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional


@dataclass
class Task:
    task_id: str
    project_id: str
    section_id: Optional[str]
    assignee_id: Optional[str]
    name: str
    description: str
    due_date: Optional[date]
    priority: str
    completed: bool
    created_at: datetime
    completed_at: Optional[datetime]

    def __post_init__(self):
        if self.completed and not self.completed_at:
            raise ValueError("Completed task must have completed_at")
        if self.completed_at and self.completed_at < self.created_at:
            raise ValueError("completed_at cannot be before created_at")
