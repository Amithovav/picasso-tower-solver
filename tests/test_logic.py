from src.logic import count_assignments
from src.models import (
    AbsoluteHint,
    RelativeHint,
    NeighborHint,
    Floor,
    Color,
    Animal,
    HINTS_EX1,
    HINTS_EX2,
    HINTS_EX3,
)

def test_example_1():
    """Tests the first original example."""
    assert count_assignments(HINTS_EX1) == 2

def test_example_2():
    """Tests the second original example."""
    assert count_assignments(HINTS_EX2) == 4

def test_example_3():
    """Tests the third original example."""
    assert count_assignments(HINTS_EX3) == 1728

def test_absolute_hint():
    """Tests a simple absolute hint."""
    hints = [AbsoluteHint(Floor.Third, Color.Red)]
    assert count_assignments(hints) == 2880

def test_neighbor_hint():
    """Tests a neighbor hint."""
    hints = [NeighborHint(Color.Red, Color.Green)]
    assert count_assignments(hints) == 5760

def test_no_hints():
    """Tests that with no hints, all 14400 assignments are valid."""
    assert count_assignments([]) == 14400

def test_contradictory_hints():
    """Tests that contradictory hints result in 0 assignments."""
    hints = [
        AbsoluteHint(Animal.Frog, Floor.First),
        AbsoluteHint(Animal.Frog, Floor.Second),
    ]
    assert count_assignments(hints) == 0