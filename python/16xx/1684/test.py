import unittest
import sys

from solution02 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
            ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
            ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.countConsistentStrings(e[0], e[1]), e[2])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.countConsistentStrings(e[0], e[1]), e[2])
            print("==================================")



if __name__ == "__main__":
    # https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    # print("Number of arguments:", len(sys.argv), "arguments.")
    # print("Argument List:", str(sys.argv))
    # if len(sys.argv) > 1:
    #     testCase = int(sys.argv[1])
    unittest.main()
