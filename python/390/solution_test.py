
import unittest

from solution03 import Solution

solution = Solution()
testCase = 5


class Test(unittest.TestCase):
    """
    def test_case0(self):
        subject = 9
        actual = solution.lastRemaining(subject)
        self.assertEqual(actual, 6)

        subject = 10
        actual = solution.lastRemaining(subject)
        self.assertEqual(actual, 8)
        subject = 2
        actual = solution.lastRemaining(subject)
        self.assertEqual(actual, 2)

        subject = 14
        actual = solution.lastRemaining(subject)
        self.assertEqual(actual, 8)
        print("===============================")

    def test_case1(self):
        subject = 4
        actual = solution.lastRemaining(subject)
        self.assertEqual(actual, 2)
        print("===============================")

    def test_case2(self):
        subject = 1
        actual = solution.lastRemaining(subject)
        self.assertEqual(actual, 1)
        print("===============================")

    def test_case3(self):
        subject = 839
        actual = solution.lastRemaining(subject)
        self.assertEqual(actual, 344)
        print("===============================")  

    def test_case4(self):
        subject = 1000000
        actual = solution.lastRemaining(subject)
        self.assertEqual(actual, 344)
        print("===============================")
    """

    def test(self):
        subjects = [
            (839, 344),
            (1000000, 481110),
            (2, 2),
            (4, 2),
            (6, 4),
            (100000000, 32896342)
        ]

        subject = subjects[testCase]
        actual = solution.lastRemaining(subject[0])
        self.assertEqual(actual, subject[1])
        print("===============================")


if __name__ == "__main__":
    unittest.main()
