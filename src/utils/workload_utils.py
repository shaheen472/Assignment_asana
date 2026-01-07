import random
from typing import List, Dict


def assign_with_load_balance(
    candidates: List[str],
    current_loads: Dict[str, int]
) -> str:
    """
    Assign work to users while avoiding overload.
    """
    sorted_users = sorted(
        candidates,
        key=lambda u: current_loads.get(u, 0)
    )
    selected = random.choice(sorted_users[: max(1, len(sorted_users)//3)])
    current_loads[selected] = current_loads.get(selected, 0) + 1
    return selected
