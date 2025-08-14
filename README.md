# Picasso Tower - Logic Puzzle Solver

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![pytest](https://img.shields.io/badge/tested%20with-pytest-blue)](https://pytest.org)

This is my solution for the Claroty "Picasso Tower" take-home exercise. The goal was to build a program that could count all valid solutions to a complex combinatorial puzzle based on a set of logical hints. This project was an opportunity to practice structured programming, testing and professional Python development workflows.

## About The Project
The Picasso Tower is a 5-story building where each floor has a unique color and is inhabited by a unique animal. With 5 colors and 5 animals, there are a total of 5! * 5! = 14,400 possible configurations.
This solver takes a list of hints (e.g., "The Rabbit lives on the first floor" or "The red floor is a neighbor of the green floor") and determines how many of the 14,400 configurations are valid.
My approach is a brute-force algorithm that generates every possible assignment and validates it against the full list of hints. The core logic is optimized with O(1) lookup maps for efficient hint evaluation.

## Key Features
-   **Object-Oriented Design:** Hints are modeled as distinct classes (`Absolute`, `Relative`, `Neighbor`), making the system clean and extensible.
-   **Optimized Solver:** While using a brute-force approach, the validation step is optimized using O(1) lookup maps for performance.
-   **Comprehensive Testing:** The solution is validated by a robust test suite using `pytest`, covering core examples, edge cases, and impossible scenarios.

## Built With
-   Python 3.9+
-   `pytest` (for testing)

