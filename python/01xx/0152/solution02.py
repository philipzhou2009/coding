# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

loggerFlag: bool = False
logger = print if loggerFlag else lambda *arg: None


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        nLen = len(nums)

        max = float("-inf")
        list1 = []

        tmpProduct = 1
        for idx, i in enumerate(nums):
            tmpProduct = tmpProduct * i
            list1.append(tmpProduct)
            max = tmpProduct if tmpProduct > max else max

        logger("list1=", list1)

        tmpList = list1
        for i in range(nLen - 1):
            tmpResult = func(tmpList[1:], nums[0])
            max = tmpResult[1] if tmpResult[1] > max else max
            tmpList = tmpResult[0]
            # logger(tmpList)

        logger("max=", max)
        return max


def func(nums: List[int], n: int) -> (List[int], int):
    max = float("-inf")
    logger("input nums=", nums)
    tmpList = []
    for i in nums:
        tmp = i if n == 0 else int(i / n)
        tmpList.append(tmp)
        max = tmp if tmp > max else max

    logger("result nums=", tmpList)
    return (tmpList, max)
