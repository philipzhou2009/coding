import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ("abcd", 2, "abcd"),
            ("deeedbbcccbdaa", 3, "aa"),
            ("pbbcggttciiippooaais", 2, "ps"),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.removeDuplicates(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.removeDuplicates(e[0], e[1]), e[2])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
