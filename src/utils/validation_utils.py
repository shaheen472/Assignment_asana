from datetime import datetime


def validate_temporal_order(
    created_at: datetime,
    completed_at: datetime
):
    if completed_at < created_at:
        raise ValueError("completed_at cannot be before created_at")


def validate_same_project(task_a_project: str, task_b_project: str):
    if task_a_project != task_b_project:
        raise ValueError("Cross-project dependency not allowed")
