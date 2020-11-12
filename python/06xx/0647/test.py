import unittest

from solution02 import Solution
from longData import longStr

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [("abc", 3), ("aaa", 6), (longStr, 500500)]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.countSubstrings(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.countSubstrings(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
