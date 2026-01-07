import uuid


def generate_uuid() -> str:
    """
    Generate UUIDv4 string to simulate Asana Global IDs (GIDs).
    """
    return str(uuid.uuid4())
