from typing import List
from models import Organization
from utils import generate_uuid, random_past_datetime
from scrapers import load_organization


def generate_organizations() -> List[Organization]:
    org_ref = load_organization()

    return [
        Organization(
            org_id=generate_uuid(),
            name=org_ref["name"],
            mail=f"contact@{org_ref['domain']}",
            created_at=random_past_datetime(start_years_ago=5)
        )
    ]
