# https://leetcode.com/problems/subsets/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        pass


def func(nums, length):

    result = []
    nLen = len(nums)
    if length == 1:
        for idx, i in enumerate(nums):
            result.append([i])

    else:
        list1 = func(nums[1:], length - 1)
        for idx, i in enumerate(list1):
            tmp = [nums[0]] + i
            print("tmpList=", tmp)
            result.append(tmp)

    print("result=", result)

    return result


nums = [1, 2, 3]
result = func(nums, 2)


def getRecuResult(abc):
    return 0
