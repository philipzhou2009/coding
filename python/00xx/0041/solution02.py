# https://leetcode.com/problems/first-missing-positive/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        logger("input=", nums)
        result = None
        if len(nums) == 0:
            result = 1
        else:
            result = getResult(nums)

        logger("result=", result)
        return result


def getResult(nums: List[int]) -> int:

    nLen = len(nums)

    vArr = [0 for i in range(nLen)]

    min = None
    max = None

    for idx, i in enumerate(nums):
        if i <= 0:
            continue

        min = i if min == None or i < min else min
        max = i if max == None or i > max else max

        if i > nLen:
            continue
        else:
            vArr[i-1] = 1

    logger("updated vArr=", vArr)
    result = None
    for idx, i in enumerate(vArr):
        if i == 0:
            result = idx + 1
            break

    result = result if result != None else max + 1

    return result

