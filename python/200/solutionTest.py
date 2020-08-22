import unittest

from solution01 import Solution
from longData import grid1, grid2

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [(grid1, 1), (grid2, 3)]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.numIslands(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.numIslands(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
