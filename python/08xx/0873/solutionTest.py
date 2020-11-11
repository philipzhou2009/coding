import unittest

from solution02 import Solution
from longData import longList1

testCase = 1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([1, 2, 3, 4, 5, 6, 7, 8], 5),
            ([1, 3, 7, 11, 12, 14, 18], 3),
            ([2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50], 5),
            ([1, 3, 5], 0),
            (longList1, 5)
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.lenLongestFibSubseq(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.lenLongestFibSubseq(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
