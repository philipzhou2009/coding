import unittest

from problem435_0 import Solution

solution = Solution()


class Test(unittest.TestCase):
    # def test_solution(self):
    #     self.assertEqual(solution.eraseOverlapIntervals(
    #         [[1, 2], [2, 3], [3, 4], [1, 3]]), 1)

    def test_case0(self):
        intervals = [[1, 2], [7, 8], [2, 3], [3, 4], [3, 10], [4, 10]]
        self.assertEqual(solution.eraseOverlapIntervals(intervals), 1)


if __name__ == '__main__':
    unittest.main()
