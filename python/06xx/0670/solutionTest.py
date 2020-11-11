import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [(2736, 7236), (9973, 9973), (277736, 77236)]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.maximumSwap(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.maximumSwap(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
