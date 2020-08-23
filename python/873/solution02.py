# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        newList = []
        i = A[-1]
        nLen = len(A)

        # counter = 0
        # while counter <= i:
        #     if not counter in A:
        #         newList.append(0)
        #     else:
        #         newList.append(counter)
        #     counter += 1

        # logger("newList=", newList)

        result = 0
        for idx, value in enumerate(A):
            tmpLen = func(A[idx:], [])
            result = tmpLen if tmpLen > result else result

        logger("result=%s" % result)

        return result

def func1(A: List[int]) -> int:
    aLen = len(A)
    if n<3:
        return 0

    maxLen = 0
    e2Idx = 1
    while e2Idx < aLen:
        e1 = A[0]
        e2 = A[e2Idx]
        tmpList = [e1, e2]

        tmpIdx = e2Idx + 1
        flag = False
        while True:
            eSum = e1 + e2
            tmpIdx = e2Idx + 1
            avail = checkAvil(A, tmpIdx, eSum)

            if avail:
                tmpList.append(eSum)
                e1 = e2
                e2 = eSum
                flag = true
                
            else:
                
            pass

def checkAvil(A: List[int], idx: int, value: int) -> bool:

    idx1 = idx
    while True:
        if A[idx1] == value:
            return True

        if A[idx1] < value:
            idx1 += 1
            continue

        if A[idx1] > value:
            return False

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

        tmpIdx = e2Idx+1
        while tmpIdx < :
            eSum = e1 + e2
            logger("e1=%s, e2=%s" % (e1, e2))

            while tmpIdx < nLen:
                tmpE = A[tmpIdx]

                if tmpE < eSum:
                    tmpIdx += 1
                    continue
                elif tmpE > eSum:
                    break
                else:
                    tmpList.append(eSum)
                    e1 = e2
                    e2 = eSum
                    break             

        logger("tmpList=", tmpList)
        tmpListLen = len(tmpList)
        maxLen = tmpListLen if tmpListLen > maxLen and tmpListLen > 2 else maxLen
        e2Idx += 1
        if e2Idx >= nLen:
            break
        e2 = A[e2Idx]

    logger("maxLen=%s" % maxLen)
    return maxLen
