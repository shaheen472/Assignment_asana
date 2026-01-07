from typing import List
from models import CustomFieldDefinition
from utils import generate_uuid, random_past_datetime


FIELDS = ["Priority", "Effort", "Risk", "Release Impact"]


def generate_custom_field_definitions(projects) -> List[CustomFieldDefinition]:
    defs = []

    for project in projects:
        for field in FIELDS[:3]:
            defs.append(
                CustomFieldDefinition(
                    field_id=generate_uuid(),
                    project_id=project.project_id,
                    name=field,
                    field_type="enum",
                    created_at=random_past_datetime(2)
                )
            )

    return defs
