"""
Solves the Picasso Tower logic puzzle.

This module provides the core logic for solving the puzzle by iterating through
all possible assignments and validating them against a given set of constraints (hints).
This version uses an O(1) lookup optimization for attribute finding.

The main public API is the `count_assignments` function.
"""
from itertools import permutations
from typing import Iterable, Optional

from .models import Floor, Color, Animal, Hint, AssignmentType, AttributeType


def count_assignments(hints: Iterable[Hint]) -> int:
    """
    Given a list of Hint objects, returns the number of
    valid assignments that satisfy all hints.
    """
    valid_count = 0
    floors = list(Floor)
    color_perms_iterator = permutations(Color)

    for color_perm in color_perms_iterator:
        animal_perms_iterator = permutations(Animal)
        for animal_perm in animal_perms_iterator:
            assignment: AssignmentType = {
                floor: (color_perm[i], animal_perm[i])
                for i, floor in enumerate(floors)
            }

            # Build O(1) lookup maps once per assignment
            color_to_floor = {color: floor for floor, (color, _) in assignment.items()}
            animal_to_floor = {animal: floor for floor, (_, animal) in assignment.items()}

            def find_floor(attr: AttributeType) -> Optional[Floor]:
                """Finds an attribute's floor using the O(1) lookup maps."""
                if isinstance(attr, Floor):
                    return attr
                if isinstance(attr, Color):
                    return color_to_floor.get(attr)
                # If not a Floor or Color, it must be an Animal
                return animal_to_floor.get(attr)

            # Pass the new, fast function to the hint evaluation logic
            if all(h.evaluate_hint(assignment, find_floor) for h in hints):
                valid_count += 1

    return valid_count