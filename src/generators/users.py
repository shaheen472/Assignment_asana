import random
from typing import List
from models import User
from utils import (
    generate_uuid, random_past_datetime,
    chance, weighted_choice
)
from scrapers import (
    load_first_names, load_last_names,
    load_role_distribution, role_to_titles
)


def generate_users(org_id: str, count: int = 2000) -> List[User]:
    users = []
    first_names = load_first_names()
    last_names = load_last_names()
    role_dist = load_role_distribution()
    titles = role_to_titles()

    for _ in range(count):
        role = weighted_choice(role_dist)
        first = random.choice(first_names)
        last = random.choice(last_names)

        users.append(
            User(
                user_id=generate_uuid(),
                org_id=org_id,
                name=f"{first} {last}",
                email=f"{first.lower()}.{last.lower()}@veeva.com",
                role=role,
                job_title=random.choice(titles[role]),
                created_at=random_past_datetime(start_years_ago=4),
                is_active=chance(0.93)
            )
        )

    return users
