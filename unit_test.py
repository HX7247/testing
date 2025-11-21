import unittest
from test_function import addition, subtraction  

class TestMyFunction(unittest.TestCase):
    # Test addition function
    def test_case_1(self):
        # Test: 2 + 3 = 5
        self.assertEqual(addition(2, 3), 5)

    def test_case_2(self):
        # Test: -1 + 1 = 0
        self.assertEqual(addition(-1, 1), 0)

    def test_case_3(self):
        # Test: 0 + 0 = 0
        self.assertEqual(addition(0, 0), 0)

    # Test subtraction function
    def test_subtraction_1(self):
        # Test: 5 - 3 = 2
        self.assertEqual(subtraction(5, 3), 2)

    def test_subtraction_2(self):
        # Test: 0 - 0 = 0
        self.assertEqual(subtraction(0, 0), 0)

    def test_subtraction_3(self):
        # Test: -1 - (-1) = 0
        self.assertEqual(subtraction(-1, -1), 0)

if __name__ == '__main__':
    # Run all unit tests
    unittest.main()