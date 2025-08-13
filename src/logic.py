"""
Solves the Picasso Tower logic puzzle.

This module provides the core logic for solving the puzzle by iterating through
all possible assignments and validating them against a given set of constraints (hints).

The main public API is the `count_assignments` function.
"""
from itertools import permutations
from typing import List, Iterable, Optional

from .models import Floor, Color, Animal, Hint, AssignmentType, AttributeType

def count_assignments(hints: Iterable[Hint]) -> int:
    """
    Given a list of Hint objects, returns the number of
    valid assignments that satisfy all hints.
    """
    def _find_floor(attr: AttributeType, assignment: AssignmentType) -> Optional[Floor]:
        """Finds the floor number of a given attribute in an assignment."""
        if isinstance(attr, Floor):
            return attr
        for floor, (color, animal) in assignment.items():
            if attr == color or attr == animal:
                return floor
        return None

    valid_count = 0
    floors = list(Floor)
    all_color_perms = permutations(Color)
    for color_perm in all_color_perms:
        for animal_perm in permutations(Animal):
            assignment: AssignmentType = {
                floor: (color_perm[i], animal_perm[i])
                for i, floor in enumerate(floors)
            }
            if all(h.evaluate_hint(assignment, _find_floor) for h in hints):
                valid_count += 1

    return valid_count