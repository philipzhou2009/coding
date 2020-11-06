import unittest

from solution02 import Solution
from longData import longStr1

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ("lee(t(c)o)de)", "lee(t(c)o)de"),
            ("a)b(c)d", "ab(c)d"),
            ("))((", ""),
            ("(a(b(c)d)", "a(b(c)d)"),
            ("ab", "ab"),
            ("(", ""),
            ("())()(((", "()()"),
            (")))t((u)", "t(u)"),
            (longStr1, "a"),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.minRemoveToMakeValid(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.minRemoveToMakeValid(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
