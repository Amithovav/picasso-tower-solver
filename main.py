from tests.test_logic import test_example_1, test_example_2, test_example_3


def run_original_tests():
    """
    Runs the three original examples from the exercise and prints a success message.
    """
    try:
        test_example_1()
        test_example_2()
        test_example_3()
        print(" Original examples passed successfully!")
    except AssertionError as e:
        print(f" A test failed: {e}")


if __name__ == "__main__":
    run_original_tests()