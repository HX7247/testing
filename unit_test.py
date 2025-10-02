import unittest
from test_function  import addition

class TestMyFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(addition(2, 3), 5)

    def test_case_2(self):
        self.assertEqual(addition(-1, 1), 0)

    def test_case_3(self):
        self.assertEqual(addition(0, 0), 0)
