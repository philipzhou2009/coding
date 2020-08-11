# https://leetcode.com/problems/rotate-function/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:

        aLen = len(A)
        if aLen <= 1:
            return 0

        newA = A.copy()
        newA.sort()
        logger("newA=", newA)
        logger("   A=", A)

        maxSum = 0
        i = 0
        while i < aLen:
            maxSum += newA[i] * i
            i += 1
            pass
        logger("maxSum=", maxSum)

        minDiff = float("inf")
        i = 0

        while i < aLen:
            if i > 0:
                # get rotated A
                # logger("A[i:]", A[i:])
                # logger("A[0:i]", A[0:i])
                tmpA = A[i:] + A[0:i]
                logger("tmpA=", tmpA)
            else:
                tmpA = A
            diff = getDiff(newA, tmpA)
            minDiff = min(minDiff, diff)
            i += 1

        logger("minDiff=", minDiff)

        result = maxSum - minDiff
        logger("result", result)

        return result


def getDiff(maxA: List[int], theList: List[int]) -> int:

    theLen = len(maxA)

    i = 0
    diff = 0
    while i < theLen:
        diff += (maxA[i] - theList[i]) * i
        i += 1
    return diff
