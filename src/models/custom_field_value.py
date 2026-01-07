from dataclasses import dataclass


@dataclass
class CustomFieldValue:
    task_id: str
    field_id: str
    value: str
