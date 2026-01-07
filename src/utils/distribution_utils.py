from .probability_utils import weighted_choice


def task_priority() -> str:
    return weighted_choice({
        "Low": 0.30,
        "Medium": 0.55,
        "High": 0.15
    })


def task_due_date_bucket() -> str:
    """
    Used to decide due date horizon.
    """
    return weighted_choice({
        "short": 0.30,     # 1–2 weeks
        "medium": 0.40,    # 1 month
        "long": 0.20,      # 1–3 months
        "none": 0.10       # no due date
    })


def project_status() -> str:
    return weighted_choice({
        "Active": 0.55,
        "Completed": 0.25,
        "On Hold": 0.10,
        "Archived": 0.10
    })


def user_role() -> str:
    return weighted_choice({
        "IC": 0.75,
        "Manager": 0.17,
        "Director": 0.05,
        "Executive": 0.03
    })


def comment_type() -> str:
    return weighted_choice({
        "comment": 0.65,
        "system": 0.35
    })
