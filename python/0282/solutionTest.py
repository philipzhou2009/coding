import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            ("123", 6, ["1+2+3", "1*2*3"]),
            ("232", 8, ["2*3+2", "2+3*2"]),
            ("105", 5, ["1*0+5", "10-5"]),
            ("00", 0, ["0+0", "0-0", "0*0"]),
            ("3456237490", 9191, []),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(set(solution.addOperators(e[0], e[1])), set(e[2]))
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.addOperators(e[0], e[1]), e[2])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
