import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [([23, 2, 4, 6, 7], 6, True), ([23, 2, 6, 4, 7], 6, True)]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.checkSubarraySum(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.checkSubarraySum(e[0], e[1]), e[2])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
