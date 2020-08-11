# https://leetcode.com/problems/integer-replacement/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def integerReplacement(self, n: int) -> int:

        result = func(n, 0)
        logger("result=", result)

        return result


def func(n, steps) -> int:

    logger("input n=", n)
    newOne = n
    i = 0
    j = 0
    k = 0
    minSteps = 0
    while newOne % 2 == 0 and newOne > 1:
        newOne = int(newOne / 2)
        i += 1
    else:
        if newOne != 1:
            j = func(newOne + 1, steps + i + 1)
            k = func(newOne - 1, steps + i + 1)
            minSteps = min(j, k) + 1

    logger("minSteps=", minSteps, ", i=", i)
    totalSteps = minSteps + i

    logger("n=", n, ", totalSteps=", totalSteps)
    return totalSteps

