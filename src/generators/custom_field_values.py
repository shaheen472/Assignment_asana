import random
from typing import List
from models import CustomFieldValue


def generate_custom_field_values(tasks, field_defs) -> List[CustomFieldValue]:
    values = []

    for task in random.sample(tasks, k=int(len(tasks) * 0.75)):
        for field in random.sample(field_defs, k=2):
            values.append(
                CustomFieldValue(
                    task_id=task.task_id,
                    field_id=field.field_id,
                    value=random.choice(["Low", "Medium", "High"])
                )
            )

    return values
