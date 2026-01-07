import random
from typing import List
from models import TeamMembership
from utils import random_past_datetime, chance


def generate_team_memberships(users, teams) -> List[TeamMembership]:
    memberships = []

    for team in teams:
        team_users = random.sample(users, k=max(5, len(users)//len(teams)))

        for user in team_users:
            memberships.append(
                TeamMembership(
                    user_id=user.user_id,
                    team_id=team.team_id,
                    joined_at=random_past_datetime(start_years_ago=3),
                    is_admin=chance(0.12)
                )
            )

    return memberships
