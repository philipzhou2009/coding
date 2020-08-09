
import unittest

from solution01 import Solution

solution = Solution()

class Test(unittest.TestCase):
    def test_case0(self):
        subject = 108
        actual = solution.lexicalOrder(subject)
        self.assertEqual(actual,  [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_case1(self):
        subject = 13
        actual = solution.lexicalOrder(subject)
        self.assertEqual(actual,  [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9])



if __name__ == "__main__":
    unittest.main()