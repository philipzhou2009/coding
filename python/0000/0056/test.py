import unittest

from solution01 import Solution

testCase = 0
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.merge(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.merge(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
