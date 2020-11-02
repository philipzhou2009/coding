import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [(8, 3), (7, 4), (1, 0), (1234, 14)]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.integerReplacement(e[0]), e[1])
                print("==================================")
        else:
            self.assertEqual(
                solution.integerReplacement(subjects[testCase][0]),
                subjects[testCase][1],
            )
            print("==================================")


if __name__ == "__main__":
    unittest.main()
