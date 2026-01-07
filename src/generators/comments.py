import random
from typing import List
from models import Comment
from utils import generate_uuid, random_past_datetime, comment_type


def generate_comments(tasks, users) -> List[Comment]:
    comments = []

    for task in random.sample(tasks, k=int(len(tasks) * 0.7)):
        for _ in range(random.randint(1, 5)):
            comments.append(
                Comment(
                    comment_id=generate_uuid(),
                    task_id=task.task_id,
                    user_id=random.choice(users).user_id,
                    type=comment_type(),
                    content="Discussion around task progress",
                    created_at=random_past_datetime(1)
                )
            )

    return comments
