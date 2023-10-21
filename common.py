from dataclasses import dataclass
from datetime import timedelta

@dataclass
class Recipe:
    title: str
    subtitle: str
    prep_time: timedelta
    cook_time: timedelta
    ingredients: list[str]
    instructions: list[str]

