import unittest
from utils.arrs import my_sum

class TestMySum(unittest.TestCase):

    def test_sum_positive_numbers(self):
        self.assertEqual(my_sum(1, 2), 3)

    def test_sum_negative_numbers(self):
        self.assertEqual(my_sum(-1, -2), -3)

    def test_sum_mixed_numbers(self):
        self.assertEqual(my_sum(1, -2), -1)

if __name__ == '__main__':
    unittest.main()