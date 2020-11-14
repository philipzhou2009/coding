# https://leetcode.com/problems/3sum/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nLen = len(nums)
        for idx, i in enumerate(nums):

            pass

        pass


def func(nums: List[int], count: int) -> List[List[int]]:

    resultList = []
    if count == 1:
        for i in nums[1:]:
            tmpList = [i]
            resultList.append(tmpList)

    else:
        # tmp = nums[0]
        for idx, i in enumerate(nums[1 : -1 * count]):
            childrenList = func(nums[1 + idx :], count - 1)
            logger("childrenList=", childrenList)

            for j in childrenList:
                resultList.append([i] + j)

    logger("resultList=", resultList)
    return resultList


func([-1, 0, 1, 2, -1, -4], 1)