import unittest
from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):

        subjects = [
            ("a", "a"),
            ("3[a]2[bc]", "aaabcbc"),
            ("3[a2[c]]", "accaccacc"),
            ("2[abc]3[cd]ef", "abcabccdcdcdef"),
            ("abc3[cd]xyz", "abccdcdcdxyz"),
        ]

        if testCase == -1:
            for theTuple in subjects:
                actual = solution.decodeString(subjects[testCase][0])
                self.assertEqual(actual, subjects[testCase][1])
                pass

        actual = solution.decodeString(subjects[testCase][0])
        self.assertEqual(actual, subjects[testCase][1])


if __name__ == "__main__":
    unittest.main()
