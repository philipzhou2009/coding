import unittest

from solution02 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([1, 2, 0], 3),
            ([3, 4, -1, 1], 2),
            ([7, 8, 9, 11, 12], 1),
            ([], 1),
            ([0], 1),
            ([1, 2, 3, 10, 2147483647, 9], 4),
            ([1], 2)
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.firstMissingPositive(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.firstMissingPositive(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
