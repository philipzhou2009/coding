import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([5, 7], 4),
            ([0, 1], 0),
            ([2, 3], 2),
            ([9, 10], 8),
            ([1, 5], 0),
            ([1, 1], 1),
            ([3, 4], 0),
            ([3, 5], 0),
            ([6, 7], 6),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.rangeBitwiseAnd(e[0][0], e[0][1]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.rangeBitwiseAnd(e[0][0], e[0][1]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
