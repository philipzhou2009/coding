import unittest

from solution01 import Solution, TreeNode
from data import *

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [(rootNode1, 6), (rootNode2, 42), (rootNode3, 2), (rootNode4, -1)]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.maxPathSum(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.maxPathSum(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
