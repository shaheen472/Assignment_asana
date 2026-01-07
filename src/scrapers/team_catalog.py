from typing import List, Dict


def load_team_catalog() -> List[Dict[str, str]]:
    """
    Enterprise SaaS team taxonomy based on real-world structures.
    """
    return [
        {"name": "Product Engineering", "function": "Engineering"},
        {"name": "Platform Engineering", "function": "Engineering"},
        {"name": "Quality Assurance", "function": "Engineering"},
        {"name": "Product Management", "function": "Product"},
        {"name": "UX Design", "function": "Product"},
        {"name": "Sales Operations", "function": "Sales"},
        {"name": "Customer Success", "function": "Customer"},
        {"name": "Marketing", "function": "Marketing"},
        {"name": "Finance", "function": "Operations"},
        {"name": "IT Operations", "function": "Operations"},
        {"name": "Security & Compliance", "function": "Operations"}
    ]
