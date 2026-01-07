import random
from typing import Dict, List, TypeVar

T = TypeVar("T")


def weighted_choice(weights: Dict[T, float]) -> T:
    """
    Select a value based on weighted probability.
    """
    choices = list(weights.keys())
    probabilities = list(weights.values())
    return random.choices(choices, probabilities)[0]


def chance(probability: float) -> bool:
    """
    Return True with given probability (0.0 - 1.0).
    """
    return random.random() < probability
