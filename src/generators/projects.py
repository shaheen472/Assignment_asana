import random
from typing import List
from models import Project
from utils import generate_uuid, random_past_datetime, project_status
from scrapers import load_project_templates


def generate_projects(org_id: str, teams) -> List[Project]:
    projects = []
    templates = load_project_templates()

    for team in teams:
        # Use semantic team function (Engineering, Product, Marketing, Operations)
        project_templates = templates.get(team.function)

        if not project_templates:
            continue  # safety guard

        for _ in range(random.randint(3, 7)):
            name = random.choice(project_templates)

            projects.append(
                Project(
                    project_id=generate_uuid(),
                    team_id=team.team_id,
                    org_id=org_id,
                    name=name,
                    description=f"{name} for enterprise delivery",
                    status=project_status(),
                    start_date=random_past_datetime(2).date(),
                    end_date=None,
                    created_at=random_past_datetime(2)
                )
            )

    return projects
