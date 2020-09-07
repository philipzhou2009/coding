import unittest

from solution01 import Solution

testCase = -1
solution = Solution()


class Test(unittest.TestCase):
    def test(self):
        subjects = [
            (123, "One Hundred Twenty Three"),
            (12345, "Twelve Thousand Three Hundred Forty Five"),
            (
                1234567,
                "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
                1234567891,
                "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One",
            ),
        ]

        if testCase == -1:
            for e in subjects:
                self.assertEqual(solution.numberToWords(e[0]), e[1])
                print("==================================")
        else:
            e = subjects[testCase]
            self.assertEqual(solution.numberToWords(e[0]), e[1])
            print("==================================")


if __name__ == "__main__":
    unittest.main()
