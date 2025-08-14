"""
Solves the Picasso Tower logic puzzle.

This module contains all the data models (Enums, Hints) and the core solving
logic for the puzzle. The main public API is the `count_assignments` function.
"""
from enum import Enum, IntEnum
from itertools import permutations
from typing import Dict, Tuple, Union, Callable, Iterable, Optional

# --- Type Aliases for Readability ---
AssignmentType = Dict["Floor", Tuple["Color", "Animal"]]
AttributeType = Union["Floor", "Color", "Animal"]
FindFloorFuncType = Callable[[AttributeType], Optional["Floor"]]

# --- Base Definitions and Enums ---
class Floor(IntEnum):
    First = 1; Second = 2; Third = 3; Fourth = 4; Fifth = 5

class Color(Enum):
    Red = "Red"; Green = "Green"; Blue = "Blue"; Yellow = "Yellow"; Orange = "Orange"

class Animal(Enum):
    Frog = "Frog"; Rabbit = "Rabbit"; Grasshopper = "Grasshopper"; Bird = "Bird"; Chicken = "Chicken"

# --- Hint Classes ---
class Hint:
    """Base class for all hint classes."""
    def evaluate_hint(self, assignment: AssignmentType, find_floor_func: FindFloorFuncType) -> bool:
        raise NotImplementedError("Each hint subclass must implement this method.")

class AbsoluteHint(Hint):
    """Represents a direct link between two attributes. Satisfied if both attributes resolve to the same floor number."""
    def __init__(self, attr1: AttributeType, attr2: AttributeType):
        self._attr1 = attr1
        self._attr2 = attr2

    def evaluate_hint(self, assignment: AssignmentType, find_floor_func: FindFloorFuncType) -> bool:
        floor1 = find_floor_func(self._attr1)
        floor2 = find_floor_func(self._attr2)
        return floor1 is not None and floor1 == floor2

class RelativeHint(Hint):
    """Represents a hint about the exact floor difference between two attributes."""
    def __init__(self, attr1: AttributeType, attr2: AttributeType, difference: int):
        self._attr1 = attr1
        self._attr2 = attr2
        self._difference = difference

    def evaluate_hint(self, assignment: AssignmentType, find_floor_func: FindFloorFuncType) -> bool:
        floor1 = find_floor_func(self._attr1)
        floor2 = find_floor_func(self._attr2)
        if floor1 is not None and floor2 is not None:
            return (floor1 - floor2) == self._difference
        return False

class NeighborHint(Hint):
    """Represents a hint where two attributes are on adjacent floors."""
    def __init__(self, attr1: AttributeType, attr2: AttributeType):
        self._attr1 = attr1
        self._attr2 = attr2

    def evaluate_hint(self, assignment: AssignmentType, find_floor_func: FindFloorFuncType) -> bool:
        floor1 = find_floor_func(self._attr1)
        floor2 = find_floor_func(self._attr2)
        if floor1 is not None and floor2 is not None:
            return abs(floor1 - floor2) == 1
        return False

# --- Main Solver Function ---
def count_assignments(hints: Iterable[Hint]) -> int:
    """
    Given a list of Hint objects, returns the number of
    valid assignments that satisfy all hints.
    """
    permutations_count = 0
    floors = list(Floor)
    color_permutations = permutations(Color)

    for color_perm in color_permutations:
        animal_permutations = permutations(Animal)
        for animal_perm in animal_permutations:
            assignment: AssignmentType = {
                floor: (color_perm[i], animal_perm[i])
                for i, floor in enumerate(floors)
            }
            color_to_floor = {color: floor for floor, (color, _) in assignment.items()}
            animal_to_floor = {animal: floor for floor, (_, animal) in assignment.items()}

            def find_floor(attr: AttributeType) -> Optional[Floor]:
                if isinstance(attr, Floor):
                    return attr
                if isinstance(attr, Color):
                    return color_to_floor.get(attr)
                return animal_to_floor.get(attr)

            if all(h.evaluate_hint(assignment, find_floor) for h in hints):
                permutations_count += 1
    return permutations_count