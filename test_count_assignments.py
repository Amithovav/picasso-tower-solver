from count_assignments import (
    count_assignments,
    AbsoluteHint,
    RelativeHint,
    NeighborHint,
    Floor,
    Color,
    Animal,
)

# Test Case Data
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

def test_example_1():
    """Tests the first original example."""
    assert count_assignments(HINTS_EX1) == 2

def test_example_2():
    """Tests the second original example."""
    assert count_assignments(HINTS_EX2) == 4

def test_example_3():
    """Tests the third original example."""
    assert count_assignments(HINTS_EX3) == 1728

def test_absolute_hint_floor_color():
    """Tests a simple absolute hint with a floor and color."""
    hints = [AbsoluteHint(Floor.Third, Color.Red)]
    assert count_assignments(hints) == 2880

def test_neighbor_hint_colors():
    """Tests a neighbor hint with two colors."""
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

def test_relative_hint_impossible_difference():
    """Tests a relative hint with an impossible difference (should be 0)."""
    hints = [RelativeHint(Color.Red, Color.Blue, 5)]
    assert count_assignments(hints) == 0

def test_neighbor_hint_impossible_distance():
    """Tests a neighbor hint between non-neighboring floors (should be 0)."""
    hints = [NeighborHint(Floor.First, Floor.Fifth)]
    assert count_assignments(hints) == 0

def test_absolute_hint_color_animal_dedicated():
    """Dedicated unit test for an absolute hint with a color and an animal."""
    hints = [AbsoluteHint(Color.Blue, Animal.Chicken)]
    assert count_assignments(hints) == 2880