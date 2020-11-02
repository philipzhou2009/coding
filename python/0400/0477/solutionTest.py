import unittest

from solution04 import Solution
from longList import longList, longList2
# from longList3 import longList3

testCase = 1
solution = Solution()

class Test(unittest.TestCase):
    def test(self):
        global longList
        subjects = [
            ([4, 14, 2], 6),
            (longList, 5861837),
            (longList2, 5846235),
            # (longList3, 10),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.totalHammingDistance(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.totalHammingDistance(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()

