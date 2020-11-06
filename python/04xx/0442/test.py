import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [([4,3,2,7,8,2,3,1], [2,3])]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.findDuplicates(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.findDuplicates(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
