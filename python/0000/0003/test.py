import unittest

from solution02 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0), ("dvdf", 3)]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.lengthOfLongestSubstring(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.lengthOfLongestSubstring(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
