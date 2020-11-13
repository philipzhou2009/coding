# https://leetcode.com/problems/group-shifted-strings/

from typing import List
from heapq import *
 
logger = print if True else lambda *arg: None


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        # s = "ab"
        # gap = int(s[0]) - int(s[1])
        # logger("gap=", gap)

        # dict1: dict = {
        #     "a": 1,
        #     "b": 2
        # }

        # logger(dict1["b"])

        H = [21, 1, 45, 78, 3, 5]
        # heapq.heapify(H)

        h = []
        for value in H:
            heappush(h, value)

        hSorted = [heappop(h) for i in range(len(h))]
        logger("h=", h)
        logger("hSorted=", hSorted)
