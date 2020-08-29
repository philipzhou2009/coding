import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            (
                [[0, 2], [5, 10], [13, 23], [24, 25]],
                [[1, 5], [8, 12], [15, 24], [25, 26]],
                [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
            ),
            ([[1, 5]], [[6, 10]], []),
            ([[1, 5]], [[0, 100]], [[1, 5]]),
            ([[1, 5]], [[0, 100], [0, 1000]], [[1, 5]]),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.intervalIntersection(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.intervalIntersection(e[0], e[1]), e[2])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
