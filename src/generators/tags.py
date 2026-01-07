from typing import List
from models import Tag
from utils import generate_uuid, random_past_datetime


TAG_NAMES = ["urgent", "backend", "frontend", "compliance", "release"]


def generate_tags() -> List[Tag]:
    return [
        Tag(
            tag_id=generate_uuid(),
            name=name,
            created_at=random_past_datetime(3)
        )
        for name in TAG_NAMES
    ]
