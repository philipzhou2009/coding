# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:

        nLen = len(A)
        result = -1
        for i in range(nLen):

            tmpResult = func(A, i + 1, K)

            if tmpResult == True:
                result = i + 1

            pass

        logger("result=", result)

        return result


def func(nums: List[int], count: int, target: int) -> bool:

    nLen = len(nums)

    result = False
    for i in range(nLen):
        logger(i)
        sum = 0

        if i + count > nLen:
            break

        # if i ==0:
        #     for j in range(count):
        #         sum = sum + nums[j]
        # else:
        for j in range(count):
            sum = sum + nums[i + j]

        logger("sum=", sum)
        if sum == target:
            result = True
            break

    return result


# func([1, 2, 3, 4, 5], 3, 10)
# Solution().shortestSubarray([1, 2, 3, 4, 5], 12)