import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            (
                ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
                [["abc", "bcd", "xyz"], ["az", "ba"], ["acef"], ["a", "z"]],
            )
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.groupStrings(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.groupStrings(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
