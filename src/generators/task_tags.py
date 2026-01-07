import random
from typing import List
from models import TaskTag


def generate_task_tags(tasks, tags) -> List[TaskTag]:
    task_tags = []

    for task in random.sample(tasks, k=int(len(tasks) * 0.5)):
        for tag in random.sample(tags, k=random.randint(1, 3)):
            task_tags.append(
                TaskTag(
                    task_id=task.task_id,
                    tag_id=tag.tag_id
                )
            )

    return task_tags
