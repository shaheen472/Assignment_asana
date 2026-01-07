from typing import List
from models import Team
from utils import generate_uuid, random_past_datetime
from scrapers import load_team_catalog


def generate_teams(org_id: str) -> List[Team]:
    teams = []
    catalog = load_team_catalog()

    for team_def in catalog:
        teams.append(
            Team(
                team_id=generate_uuid(),
                org_id=org_id,
                name=team_def["name"],
                description=f"{team_def['function']} team at enterprise scale",
                function=team_def["function"],
                created_at=random_past_datetime(start_years_ago=4)
            )
        )

    return teams
