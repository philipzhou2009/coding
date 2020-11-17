# https://leetcode.com/problems/first-missing-positive/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        result = None
        if len(nums) == 0:
            result = 1
        else:
            result = getResult(nums)

        logger("result=", result)
        return result


def getResult(nums: List[int]) -> int:

    min = None
    max = None

    total = 0
    for idx, i in enumerate(nums):
        if i <= 0:
            continue
        min = i if min == None or i < min else min
        max = i if max == None or i > max else max
        # total = total + i
        pass

    logger("min=", min, "max=", max, "total=", total)

    if min == None or min > 1 :
        return 1

    vArr = [0 for i in range(max)]
    logger("vArr=", vArr)

    for i in nums:
        if i <= 0:
            continue
        vArr[i - 1] = 1

    logger("updated vArr=", vArr)

    result = None
    for idx, i in enumerate(vArr):
        if i == 0:
            result = idx + 1
            break
        pass
    pass

    result = max + 1 if result == None else result

    return result


# getResult([7, 8, 9, 11, 12])

