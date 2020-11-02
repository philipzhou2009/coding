import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ("12", 2),
            ("226", 3),
            ("0", 0),
            ("1", 1),
            ("002", 1),
            ("1111", 5),
            ("2101", 1),
            # ("1020", 1),
            ("101020", 1),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.numDecodings(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.numDecodings(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
