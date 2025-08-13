from itertools import permutations
from typing import List, Union, Any

# הנקודה .models אומרת לפייתון לייבא מהקובץ models.py שנמצא באותה תיקייה (src)
from .models import Floor, Color, Animal, Hint, AssignmentType, AttributeType

def count_assignments(hints: List[Hint]) -> int:
    """
    Given a list of Hint objects, returns the number of
    valid assignments that satisfy all hints.
    """
    def _find_floor(attr: AttributeType, assignment: AssignmentType) -> Union[Floor, None]:
        """Finds the floor number of a given attribute in an assignment."""
        if isinstance(attr, Floor):
            return attr
        for floor, (color, animal) in assignment.items():
            if attr == color or attr == animal:
                return floor
        return None

    valid_count = 0
    floors = list(Floor)
    all_color_perms = list(permutations(Color))
    all_animal_perms = list(permutations(Animal))

    for color_perm in all_color_perms:
        for animal_perm in all_animal_perms:
            assignment: AssignmentType = {
                floor: (color_perm[i], animal_perm[i])
                for i, floor in enumerate(floors)
            }
            if all(h.evaluate_hint(assignment, _find_floor) for h in hints):
                valid_count += 1

    return valid_count