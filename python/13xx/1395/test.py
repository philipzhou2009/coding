import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [([2, 5, 3, 4, 1], 3), ([2, 1, 3], 0), ([1, 2, 3, 4])]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.numTeams(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.numTeams(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
