import unittest

from solution01 import Solution

testCase = 0
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([], []),
            ([0], []),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.threeSum(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.threeSum(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
