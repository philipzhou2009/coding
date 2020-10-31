import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [([9,9,6,0,6,6,9], 3)]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.longestWPI(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.longestWPI(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
