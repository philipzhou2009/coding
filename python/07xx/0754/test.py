import unittest

from solution01 import Solution

testCase = 4
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [(3, 2), (2, 3), (0, 0), (-3, 2), (-1000000000, 1000)]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.reachNumber(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.reachNumber(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
