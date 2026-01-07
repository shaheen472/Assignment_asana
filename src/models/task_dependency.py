from dataclasses import dataclass
from datetime import datetime


@dataclass
class TaskDependency:
    dependency_id: str
    blocking_task_id: str
    blocked_task_id: str
    created_at: datetime
