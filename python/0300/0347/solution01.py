# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List

# from collections import deque

logger = print if False else lambda *arg: None


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nLen = len(nums)
        dict1 = {}
        for idx, i in enumerate(nums):
            # logger("i=", i)
            v = dict1.get(i)
            dict1[i] = 1 if v == None else v + 1

        logger("dict1=", dict1)

        result = []

        i = 0
        while i < k:
            mCount = None
            mKey = None
            for key in dict1.keys():
                val = dict1.get(key)
                if mCount == None or val > mCount:
                    mCount = val
                    mKey = key
                pass

            result.append(mKey)
            dict1[mKey] = -1
            i = i + 1

        logger("result=", result)     

        return result
