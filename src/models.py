from enum import Enum, IntEnum
from typing import List, Dict, Tuple, Any, Union

# --- Type Aliases for Readability ---
# Note: Using strings for forward references to avoid circular import issues if ever needed.
AssignmentType = Dict["Floor", Tuple["Color", "Animal"]]
AttributeType = Union["Floor", "Color", "Animal"]

# --- Base Definitions and Enums ---

class Floor(IntEnum):
    First = 1
    Second = 2
    Third = 3
    Fourth = 4
    Fifth = 5

class Color(Enum):
    Red = "Red"
    Green = "Green"
    Blue = "Blue"
    Yellow = "Yellow"
    Orange = "Orange"

class Animal(Enum):
    Frog = "Frog"
    Rabbit = "Rabbit"
    Grasshopper = "Grasshopper"
    Bird = "Bird"
    Chicken = "Chicken"

# --- Hint Classes ---

class Hint:
    """Base class for all hint classes."""
    def evaluate_hint(self, assignment: AssignmentType, _find_floor_func: Any) -> bool:
        """Evaluates if the hint is satisfied by a given assignment."""
        raise NotImplementedError("Each hint subclass must implement this method.")

class AbsoluteHint(Hint):
    """Represents a hint where two attributes must be on the same floor."""
    def __init__(self, attr1: AttributeType, attr2: AttributeType):
        self._attr1 = attr1
        self._attr2 = attr2

    def evaluate_hint(self, assignment: AssignmentType, _find_floor_func: Any) -> bool:
        """Evaluates an absolute hint: both attributes must be on the same floor."""
        floor1 = _find_floor_func(self._attr1, assignment)
        floor2 = _find_floor_func(self._attr2, assignment)
        return floor1 is not None and floor1 == floor2

class RelativeHint(Hint):
    """Represents a hint about the exact floor difference between two attributes."""
    def __init__(self, attr1: AttributeType, attr2: AttributeType, difference: int):
        self._attr1 = attr1
        self._attr2 = attr2
        self._difference = difference

    def evaluate_hint(self, assignment: AssignmentType, _find_floor_func: Any) -> bool:
        """Evaluates a relative hint: the difference between the attributes' floors must match."""
        floor1 = _find_floor_func(self._attr1, assignment)
        floor2 = _find_floor_func(self._attr2, assignment)
        if floor1 is not None and floor2 is not None:
            return (floor1 - floor2) == self._difference
        return False

class NeighborHint(Hint):
    """Represents a hint where two attributes are on adjacent floors."""
    def __init__(self, attr1: AttributeType, attr2: AttributeType):
        self._attr1 = attr1
        self._attr2 = attr2

    def evaluate_hint(self, assignment: AssignmentType, _find_floor_func: Any) -> bool:
        """Evaluates a neighbor hint: the absolute difference between the attributes' floors must be 1."""
        floor1 = _find_floor_func(self._attr1, assignment)
        floor2 = _find_floor_func(self._attr2, assignment)
        if floor1 is not None and floor2 is not None:
            return abs(floor1 - floor2) == 1
        return False

# --- Test Case Data ---

HINTS_EX1 = [
    AbsoluteHint(Animal.Rabbit, Floor.First),
    AbsoluteHint(Animal.Chicken, Floor.Second),
    AbsoluteHint(Floor.Third, Color.Red),
    AbsoluteHint(Animal.Bird, Floor.Fifth),
    AbsoluteHint(Animal.Grasshopper, Color.Orange),
    NeighborHint(Color.Yellow, Color.Green),
]

HINTS_EX2 = [
    AbsoluteHint(Animal.Bird, Floor.Fifth),
    AbsoluteHint(Floor.First, Color.Green),
    AbsoluteHint(Animal.Frog, Color.Yellow),
    NeighborHint(Animal.Frog, Animal.Grasshopper),
    NeighborHint(Color.Red, Color.Orange),
    RelativeHint(Animal.Chicken, Color.Blue, -4),
]

HINTS_EX3 = [RelativeHint(Animal.Rabbit, Color.Green, -2)]