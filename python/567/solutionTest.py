import unittest

from solution02 import Solution
from longData import longStr1, longStr2, longStr3, longStr4

testCase = 6
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ("ab", "eidbaooo", True),
            ("ab", "eidboaoo", False),
            ("adc", "dcda", True),
            (longStr1, longStr2, True),
            ("abc", "aaaaaaaaaaabc", True),
            ("hello", "ooolleoooleh", False),
            (longStr3, longStr4, True),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.checkInclusion(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.checkInclusion(e[0], e[1]), e[2])
            print("==================================")

    # def assertFucn(self, )


if __name__ == "__main__":
    unittest.main()

