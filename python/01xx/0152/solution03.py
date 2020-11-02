# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

loggerFlag: bool = True
logger = print if loggerFlag else lambda *arg: None


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        nLen = len(nums)

        max = float("-inf")
        zerolist = []

        lastZeroIdx = None
        for i in range(nLen):
            if nums[i] == 0:
                zerolist.append(i)

        logger("zerolist=", zerolist)

        for idx, i in enumerate(nums):
            if i == 0:
                if lastZeroIdx == None:
                    tmp = meaningfulFunc(nums[0:idx])
                else:
                    tmp = meaningfulFunc(nums[lastZeroIdx + 1 : idx])

                lastZeroIdx = idx
                max = tmp if tmp > max else max

            if idx == nLen - 1 and not lastZeroIdx == None:
                tmp = meaningfulFunc(nums[lastZeroIdx + 1 :])
                max = tmp if tmp > max else max

        if not lastZeroIdx == None:
            max = max if max > 0 else 0

        if lastZeroIdx == None:
            max = meaningfulFunc(nums)

        return max


def meaningfulFunc(nums: List[int]) -> int:
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
