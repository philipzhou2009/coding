import unittest

from solution01 import Solution

testCase = 7
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            (10, 3, 3),
            (7, -3, -2),
            (-8, 3, -2),
            (9, 3, 3),
            (5, 10, 0),
            (-5, 10, 0),
            (-2147483648, -1, 2147483647),
            (-50000000, -1, 50000000),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.divide(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.divide(e[0], e[1]), e[2])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
