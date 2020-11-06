# https://leetcode.com/problems/total-hamming-distance/

from typing import List

from collections import Counter

logger = print if False else lambda *arg: None


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        result = 0
        nLen = len(nums)
        dict1 = {}

        for i in nums:
            arr = func(i)
            dict1[i] = arr
            pass

        logger(dict1)

        for idx1, v1 in enumerate(nums):

            arr1 = dict1[v1]
            idx2 = idx1 + 1

            while idx2 < nLen:
                v2 = nums[idx2]
                idx2 += 1
                arr2 = dict1[v2]
                arrXor = arr1 ^ arr2

                logger("arrXor len=%s" % len(arrXor))
                result += len(arrXor)

        logger("result=%s" % result)
        return result


def func(input: int) -> List[int]:

    i = input
    cursor = 0
    result0 = []
    result = set()
    while i != 0:
        if i % 2 == 1:
            result.add(cursor)
            i -= 1
        else:
            i /= 2
            cursor += 1

    logger(result)
    return result
