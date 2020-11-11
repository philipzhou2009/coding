# https://leetcode.com/problems/merge-intervals/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        pass


def func(intervals: List[List[int]]) -> List[List[int]]:
    sortedIntervals = sorted(intervals, key=lambda item: item[1])

    logger("sortedIntervals=", sortedIntervals)

    
    pass


func([[1, 3], [8, 10], [2, 6], [15, 18]])