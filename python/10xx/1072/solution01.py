# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

from typing import List
from collections import Counter

logger = print if True else lambda *arg: None


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        logMatrix(matrix)

        newList = []
        for e in matrix:
            tmpList = e
            if e[0] == 0:
                tmpList = zeroToOne(e)

            str1 = listToInt(tmpList)
            logger("str1=%s" % str1)
            newList.append(str1)
            pass

        c = Counter(newList)
        logger("counter=", c)

        mostCommon = c.most_common(1)
        logger("mostCommon=", mostCommon)

        return mostCommon[0][1]


def zeroToOne(inputList: List[int]) -> List[int]:

    tmpList = []
    for idx, value in enumerate(inputList):
        tmp = 1 if value == 0 else 0
        tmpList.append(tmp)

    return tmpList


def listToInt(inputList: List[int]) -> str:

    result = ""
    for e in inputList:
        result += str(e)
        pass
    return result


def logMatrix(matrix):

    for e in matrix:
        logger(e)
        pass

