import random
from typing import List
from models import Task
from utils import (
    generate_uuid, random_past_datetime,
    task_priority, chance, ensure_after
)


def generate_tasks(projects, sections, users) -> List[Task]:
    tasks = []

    for project in projects:
        project_sections = [s for s in sections if s.project_id == project.project_id]

        for _ in range(random.randint(20, 60)):
            created_at = random_past_datetime(1)
            completed = chance(0.65)
            completed_at = ensure_after(created_at) if completed else None

            tasks.append(
                Task(
                    task_id=generate_uuid(),
                    project_id=project.project_id,
                    section_id=random.choice(project_sections).section_id,
                    assignee_id=random.choice(users).user_id if chance(0.85) else None,
                    name="Implement feature logic",
                    description="Detailed task description",
                    due_date=None,
                    priority=task_priority(),
                    completed=completed,
                    created_at=created_at,
                    completed_at=completed_at
                )
            )

    return tasks
