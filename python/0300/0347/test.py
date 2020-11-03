import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [([1,1,1,2,2,3], 2, [1, 2]), ([1], 1, [1])]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.topKFrequent(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.topKFrequent(e[0], e[1]), e[2])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
