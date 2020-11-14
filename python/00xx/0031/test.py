import unittest

from solution02 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([1, 2, 3], [1, 3, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([1, 1, 5], [1, 5, 1]),
            ([1], [1]),
            ([1, 3, 2], [2, 1, 3]),
            ([1, 2, 4, 3], [1, 3, 2, 4]),
        ]

        if testCase == -1:
            for e in subjects:
                solution.nextPermutation(e[0])
                print("e[0]=", e[0])
                self.assertEqual(e[0], e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            solution.nextPermutation(e[0])
            self.assertEqual(e[0], e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
