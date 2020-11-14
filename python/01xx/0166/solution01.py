# https://leetcode.com/problems/fraction-to-recurring-decimal/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        f1 = numerator / denominator
        logger("f1=", f1)
        s1 = str(f1)
        logger("s1=", s1)

        sArr = s1.split(".")

        logger("subs=", sArr)

        foundDup = func(sArr[1])

        sNew = foundDup if len(foundDup) == len(sArr[1]) else "(" + foundDup + ")"

        sFinal = sArr[0] + "." + sNew

        logger("result=", sFinal)

        return sFinal


def func(s: str) -> str:

    sLen = len(s)
    half = int(sLen / 2)

    result = None
    for i in range(1, half + 1):
        tmpResult = isDup(s, i)
        if tmpResult == True:
            result = s[0 : 0 + i]
            break

    result = s if result == None else result

    logger("found dup=", result)
    return result


def isDup(s: str, i: int) -> bool:
    sLen = len(s)

    firstOne = s[0:i]
    cursor = 0
    result = True
    while True:
        if cursor + i > sLen:
            break
        tmpStr = s[cursor : cursor + i]
        logger("tmpStr=", tmpStr)
        if not tmpStr == firstOne:
            result = False
            break
        else:
            cursor = cursor + i

    logger("isDup=", result)
    return result


# isDup("012012012012012012", 3)
# func("5545")

