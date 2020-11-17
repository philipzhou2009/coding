import unittest

from solution01 import Solution
from longData import longData

testCase = 5
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9),
            ([0], 0),
            ([1], 0),
            ([0, 0], 0),
            (longData, 10),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.trap(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.trap(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
