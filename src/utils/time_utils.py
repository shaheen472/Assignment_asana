import random
from datetime import datetime, timedelta, date
from typing import Optional


def random_past_datetime(
    start_years_ago: int = 5,
    end_days_ago: int = 0
) -> datetime:
    """
    Generate a random datetime within a realistic enterprise history window.
    """
    now = datetime.utcnow()
    start = now - timedelta(days=365 * start_years_ago)
    end = now - timedelta(days=end_days_ago)

    delta_seconds = int((end - start).total_seconds())
    return start + timedelta(seconds=random.randint(0, delta_seconds))


def random_future_date(
    min_days: int,
    max_days: int
) -> date:
    """
    Generate a future date used for due dates and project timelines.
    """
    return (datetime.utcnow() + timedelta(
        days=random.randint(min_days, max_days)
    )).date()


def ensure_after(
    earlier: datetime,
    min_days: int = 1,
    max_days: int = 14
) -> datetime:
    """
    Ensure a timestamp occurs after another timestamp.
    Used for completed_at, joined_at, comments, dependencies.
    """
    return earlier + timedelta(days=random.randint(min_days, max_days))
