import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
            ([2, 0, 1], [0, 1, 2]),
            ([0], [0]),
            ([1], [1]),
        ]

        if testCase == -1:
            for e in subjects:
                solution.sortColors(e[0])
                self.assertEqual(e[0], e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            solution.sortColors(e[0])
            self.assertEqual(e[0], e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
