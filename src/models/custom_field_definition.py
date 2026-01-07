from dataclasses import dataclass
from datetime import datetime


@dataclass
class CustomFieldDefinition:
    field_id: str
    project_id: str
    name: str          # e.g. Priority, Effort, Risk
    field_type: str    # e.g. enum, number, text
    created_at: datetime
