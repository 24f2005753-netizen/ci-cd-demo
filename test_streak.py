import unittest
from streak import longest_positive_streak

class TestLongestPositiveStreak(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(longest_positive_streak([]), 0)

    def test_no_positive_numbers(self):
        self.assertEqual(longest_positive_streak([-1, -2, -3]), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(longest_positive_streak([1, 2, 3]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(longest_positive_streak([1, 2, -3, 4, 5, 6]), 3)

    def test_streaks_at_beginning_and_end(self):
        self.assertEqual(longest_positive_streak([1, 2, 3, -1, -2, 4, 5]), 3)
        self.assertEqual(longest_positive_streak([1, 2, -1, -2, 3, 4, 5]), 3)

if __name__ == '__main__':
    unittest.main()