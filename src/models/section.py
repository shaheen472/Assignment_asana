from dataclasses import dataclass


@dataclass
class Section:
    section_id: str
    project_id: str
    name: str
    position: int
