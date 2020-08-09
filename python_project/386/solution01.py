# https://leetcode.com/problems/lexicographical-numbers/
from typing import List

logger = print if False else lambda *arg: None

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        nStr = str(n)
        nLen = len(nStr)
        logger("nLen", nLen)
        i = 1
        tmpList = []
        while True:
            iStr = str(i)
            iStrPadZero = iStr.ljust(nLen, '0')
            logger(iStrPadZero)
            tmpTuple = (i, iStrPadZero)
            tmpList.append(tmpTuple)
            i += 1
            if i > n:
                break

            pass

        logger("tmpList org ", tmpList)
        tmpList.sort(key=sort)
        logger("tmpList sort", tmpList)

        resultList = []
        for ce in tmpList:
            resultList.append(ce[0])
            pass

        logger("resultList", resultList)

        return resultList


def sort(e):
    return e[1]
