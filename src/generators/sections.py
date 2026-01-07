from typing import List
from models import Section
from utils import generate_uuid


DEFAULT_SECTIONS = [
    "Backlog", "To Do", "In Progress", "In Review", "Done"
]


def generate_sections(projects) -> List[Section]:
    sections = []

    for project in projects:
        for idx, name in enumerate(DEFAULT_SECTIONS):
            sections.append(
                Section(
                    section_id=generate_uuid(),
                    project_id=project.project_id,
                    name=name,
                    position=idx + 1
                )
            )

    return sections
