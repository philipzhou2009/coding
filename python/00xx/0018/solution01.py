# https://leetcode.com/problems/4sum/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        combs = getCombinations(nums, 4)
        resultList = []
        for t in combs:

            if t[0] + t[1] + t[2] + t[3] == target:
                resultList.append(t)
            pass

        logger("result=", resultList)
        return resultList


def getCombinations(nums: List[int], count: int) -> List[List[int]]:

    nLen = len(nums)

    resultList = []
    if count == 1:
        for i in nums:
            resultList.append([i])
        return resultList

    for i in range(nLen - count + 1):
        # logger("i=", i)
        tmpList = getCombinations(nums[i + 1 :], count - 1)
        for t in tmpList:
            t1 = [nums[i]] + t
            resultList.append(t1)

    return resultList


# getCombinations([1, 0, -1, 0, -2, 2], 4)
# logger(getCombinations([1, 2, 3, 4, 5, 6], 4))
