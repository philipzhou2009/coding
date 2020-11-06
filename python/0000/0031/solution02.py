# https://leetcode.com/problems/next-permutation/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        logger("input=", nums)

        nLen = len(nums)
        flag = True

        for idx in range(nLen - 1, -1, -1):
            logger("idx=", idx)

            if idx - 1 < 0:
                flag = False
                break

            v1 = nums[idx]
            v2 = nums[idx - 1]
            if v1 > v2:
                flag = True
                nums = func(nums, idx - 1)
                break

        if flag == False:
            nums.sort()

        logger("nums=", nums)
        pass


def func(nums: List[int], idx: int) -> List[int]:

    numsP1 = nums[0:idx]
    numsP2 = nums[idx:]

    sortedP2 = sorted(numsP2)
    logger(numsP1, numsP2, sortedP2)

    tmp = sortedP2[0]
    sortedP2[0] = sortedP2[1]
    sortedP2[1] = tmp
    logger("after swap=", sortedP2)

    result = numsP1 + sortedP2
    logger("result=", result)
    return result


# func([1, 2, 4, 3], 1)
# func([1, 2, 3, 4], 2)

