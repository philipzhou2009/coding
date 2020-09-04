import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [("cbaebabacd", "abc", [0, 6]), ("abab", "ab", [0, 1, 2])]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.findAnagrams(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.findAnagrams(e[0], e[1]), e[2])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
