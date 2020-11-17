# https://leetcode.com/problems/minimum-window-substring/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass


def getResult(s: str, t: str) -> str:

    newStr = ""

    for c in s:
        if c in t:
            newStr = newStr + c
        else:
            newStr = newStr + "X"

    logger("newStr=", newStr)

    tLen = len(t)
    sLen = len(s)

    for tmpLen in range(tLen, sLen + 1):
        logger("new set---")
        for i in range(0, sLen - tmpLen + 1):
            logger("testing str=", newStr[i : i + tmpLen])

            

            pass

    pass


getResult("ADOBECODEBANC", "ABC")

