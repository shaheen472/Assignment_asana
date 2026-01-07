from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Subtask:
    subtask_id: str
    parent_task_id: str
    assignee_id: Optional[str]
    name: str
    completed: bool
    created_at: datetime
    completed_at: datetime

    def __post_init__(self):
        if self.completed and not self.completed_at:
            raise ValueError("Completed subtask must have completed_at")
