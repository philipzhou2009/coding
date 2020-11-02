# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

loggerFlag: bool = True
logger = print if loggerFlag else lambda *arg: None


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        nLen = len(nums)

        result = float("-inf")
        for i in range(nLen):
            tmpProduct = func(nums[i:])
            logger("tmpProduct=", tmpProduct)
            result = tmpProduct if tmpProduct > result else result
            pass


        logger("result=", result)
        return result


def func(nums: List[int]) -> int:

    product = float("-inf")

    tmpProduct = 1
    for idx, i in enumerate(nums):
        tmpProduct = tmpProduct * i
        if tmpProduct < product:
            break
        else:
            product = tmpProduct
        pass

    return product
