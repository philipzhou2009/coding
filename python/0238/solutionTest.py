import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([2, 3, 4], [12, 8, 6]),
            ([2, 3, 4, 5], [60, 40, 30, 24]),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.productExceptSelf(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.productExceptSelf(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
