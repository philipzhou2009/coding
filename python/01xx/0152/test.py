import unittest

from solution03 import Solution

testCase = 5
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([2, 3, -2, 4], 6),
            ([-2, 0, -1], 0),
            ([-2, 3, -4], 24),
            ([0, 2], 2),
            ([1, 0, 2, 0, 3], 3),
            ([3, -1, 4], 4),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.maxProduct(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.maxProduct(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
