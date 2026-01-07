import random
from typing import List
from faker import Faker

from models import User
from utils import (
    generate_uuid,
    random_past_datetime,
    chance,
    weighted_choice
)
from scrapers import (
    load_role_distribution,
    role_to_titles
)


def generate_users(org_id: str, count: int = 2000) -> List[User]:
    """
    Generate realistic enterprise users using Faker.

    Guarantees:
    - Human-like names
    - Unique emails per user
    - Scales to thousands of users (7,500+)
    - Respects database UNIQUE(org_id, email) constraint
    """

    fake = Faker()
    Faker.seed(42)  # reproducibility for evaluation

    users: List[User] = []
    role_dist = load_role_distribution()
    titles = role_to_titles()

    for user_index in range(1, count + 1):
        role = weighted_choice(role_dist)

        # Generate realistic human name
        full_name = fake.name()

        # Generate unique enterprise email
        email = fake.unique.email()
        email = email.replace("@example.com", "@veeva.com")

        users.append(
            User(
                user_id=generate_uuid(),
                org_id=org_id,
                name=full_name,
                email=email,
                role=role,
                job_title=random.choice(titles[role]),
                created_at=random_past_datetime(start_years_ago=4),
                is_active=chance(0.93)
            )
        )

    return users
