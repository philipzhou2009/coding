import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
            ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
            ([], 0, [-1, -1]),
            ([2, 2], 2, [0, 1]),
            ([1, 3], 1, [0, 0]),
            ([1, 4], 4, [1, 1]),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.searchRange(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.searchRange(e[0], e[1]), e[2])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
