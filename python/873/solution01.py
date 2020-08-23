# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        newList = []
        i = A[-1]
        nLen = len(A)

        counter = 0
        while counter <= i:
            if not counter in A:
                newList.append(0)
            else:
                newList.append(counter)
            counter += 1

        logger("newList=", newList)

        fiboList = []

        result = 0
        for idx, value in enumerate(A):
            tmpLen = func(A[idx:], newList)
            result = tmpLen if tmpLen > result else result

        logger("result=%s" % result)

        return result


def func(A: List[int], newList: List[int]) -> List:
    nLen = len(A)

    if nLen < 3:
        return 0

    maxLen = 0
    e2Idx = 1
    while True:
        e1 = A[0]
        e2 = A[e2Idx]
        tmpList = [e1, e2]

        while True:
            eSum = e1 + e2
            logger("e1=%s, e2=%s" % (e1, e2))
            if eSum > A[-1] or newList[eSum] == 0:
                logger("breakpoint=%s" % eSum)
                break
            else:
                tmpList.append(eSum)

            e1 = e2
            e2 = eSum

        logger("tmpList=", tmpList)
        tmpListLen = len(tmpList)
        maxLen = tmpListLen if tmpListLen > maxLen and tmpListLen > 2 else maxLen
        e2Idx += 1
        if e2Idx >= nLen:
            break
        e2 = A[e2Idx]

    logger("maxLen=%s" % maxLen)
    return maxLen
