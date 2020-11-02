# https://leetcode.com/problems/ones-and-zeroes/

from typing import List

from collections import Counter

logger = print if True else lambda *arg: None


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        totalZeros = 0
        totalOnes = 0

        for str in strs:
            tmp = getZerosAndOnes(str)
            logger(tmp)
            totalZeros += tmp[0]
            totalOnes += tmp[1]
            pass

        logger("zeros=%s, ones=%s" % (totalZeros, totalOnes))
        return getLen(strs, m, n, totalZeros, totalOnes)


def getLen(strs: List[str], m: int, n: int, totalZeros: int, totalOnes: int) -> int:

    logger(
        "strs=%s, m=%s, n=%s, totalZeros=%s, totalOnes=%s"
        % (strs, m, n, totalZeros, totalOnes)
    )

    resultLen = 0
    if m >= totalZeros and n >= totalOnes:
        resultLen = len(strs)
        logger("resultLen=", resultLen)
        return resultLen

    if totalZeros - m >= totalOnes - n:
        strs.sort(key=arraySortByZeros, reverse=True)
    else:
        strs.sort(key=arraySortByOnes, reverse=True)

    logger("sorted=%s" % strs)

    str0ZerosAndOnes = getZerosAndOnes(strs[0])

    strs.pop(0)

    return getLen(
        strs, m, n, totalZeros - str0ZerosAndOnes[0], totalOnes - str0ZerosAndOnes[1]
    )


def arraySortByZeros(input: str) -> tuple:
    i = 0
    zeros = 0
    ones = 0

    logger("forLoop in str")

    counter = Counter()
    for c in input:
        logger(c)
        counter[c] += 1

    logger("counter", counter)

    while i < len(input):
        c = input[i]
        if c == "0":
            zeros += 1

        if c == "1":
            ones += 1

        # logger("c=", c)
        i += 1



    return (zeros, ones)


def arraySortByOnes(input: str) -> tuple:
    i = 0
    zeros = 0
    ones = 0
    while i < len(input):
        c = input[i]
        if c == "0":
            zeros += 1

        if c == "1":
            ones += 1

        # logger("c=", c)
        i += 1

    return (ones, zeros)


def getZerosAndOnes(input: str) -> int:

    i = 0
    zeros = 0
    ones = 0
    while i < len(input):
        c = input[i]
        if c == "0":
            zeros += 1

        if c == "1":
            ones += 1

        # logger("c=", c)
        i += 1

    return (zeros, ones)

