from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass
class ActivityItem:
    """
    Data object representing a single activity
    """
    key: str
    full_name: str


class Activity(Enum):
    """
    Enum for the different types of activities
    """
    # specify type of value for type hints
    value: ActivityItem

    # all activities
    youtube = ActivityItem("youtube", "YouTube Together")
    poker = ActivityItem("poker", "Poker Night")
    chess = ActivityItem("chess", "Chess in the Park")
    betrayal = ActivityItem("betrayal", "Betrayal.io")
    fishing = ActivityItem("fishing", "Fishington.io")
    letter_tile = ActivityItem("letter-tile", "Letter Tile")
    word_snack = ActivityItem("word-snack", "Word Snack")
    doodle_crew = ActivityItem("doodle-crew", "Doodle Crew")

    @classmethod
    def get_activity(cls, key) -> Optional["Activity"]:
        """
        Get an activity by key
        """
        for activity in cls:
            if activity.value.key == key:
                return activity
        return None