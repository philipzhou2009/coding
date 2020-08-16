import unittest

from solution01 import Solution

testCase = 4
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            (["01", "00", "11", "0101"], 2, 2, 2),
            (["10", "0001", "111001", "1", "0"], 5, 3, 4),
            (["10", "0", "1"], 1, 1, 2),
            (["10", "0001", "111001", "1", "0"], 4, 3, 3),
            (["1100", "100000", "011111"], 6, 6, 2),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.findMaxForm(e[0], e[1], e[2]), e[3])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.findMaxForm(e[0], e[1], e[2]), e[3])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
