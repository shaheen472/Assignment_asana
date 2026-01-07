import random
from typing import List
from models import TaskDependency
from utils import generate_uuid, random_past_datetime


def generate_task_dependencies(tasks) -> List[TaskDependency]:
    deps = []

    for task in random.sample(tasks, k=int(len(tasks) * 0.25)):
        blocker = random.choice(tasks)
        if blocker.project_id != task.project_id:
            continue

        deps.append(
            TaskDependency(
                dependency_id=generate_uuid(),
                blocking_task_id=blocker.task_id,
                blocked_task_id=task.task_id,
                created_at=random_past_datetime(1)
            )
        )

    return deps
