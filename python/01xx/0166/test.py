import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            (1, 2, "0.5"),
            (2, 1, "2"),
            (2, 3, "0.(6)"),
            (4, 333, "0.(012)"),
            (1, 5, "0.2"),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.fractionToDecimal(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.fractionToDecimal(e[0], e[1]), e[2])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
