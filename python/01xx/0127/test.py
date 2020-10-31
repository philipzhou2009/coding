import unittest

# from solution01 import Solution
from solution02 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            (5, True),
            (3, False),
            (4, True),
            (2, True),
            (1, True),
            (100000000, True),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.judgeSquareSum(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.judgeSquareSum(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
