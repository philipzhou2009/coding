import unittest

from solution01 import Solution

testCase = 2
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([[0, 1], [1, 1]], 1),
            ([[0, 1], [1, 0]], 2),
            ([[0, 0, 0], [0, 0, 1], [1, 1, 0]], 2),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.maxEqualRowsAfterFlips(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.maxEqualRowsAfterFlips(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
