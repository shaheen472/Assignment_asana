import random
from typing import List
from models import Subtask
from utils import generate_uuid, ensure_after


def generate_subtasks(tasks) -> List[Subtask]:
    subtasks = []

    for task in random.sample(tasks, k=len(tasks)//3):
        for _ in range(random.randint(1, 4)):
            completed = random.choice([True, False])

            subtasks.append(
                Subtask(
                    subtask_id=generate_uuid(),
                    parent_task_id=task.task_id,
                    assignee_id=task.assignee_id,
                    name="Subtask breakdown",
                    completed=completed,
                    created_at=task.created_at,
                    completed_at=ensure_after(task.created_at) if completed else None
                )
            )

    return subtasks
