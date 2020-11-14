import unittest

from solution02 import Solution
from longData import longData01

testCase = 5
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([3, 1, 4, 1, 5], 2, 2),
            ([1, 2, 3, 4, 5], 1, 4),
            ([1, 3, 1, 5, 4], 0, 1),
            ([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3, 2),
            ([-1, -2, -3], 1, 2),
            (longData01, 1, 2)
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.findPairs(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.findPairs(e[0], e[1]), e[2])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
