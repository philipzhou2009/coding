import unittest

from solution03 import Solution

testCase = 3
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [(10, 4), (0, 0), (1, 0), (499979, 41537)]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.countPrimes(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.countPrimes(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
