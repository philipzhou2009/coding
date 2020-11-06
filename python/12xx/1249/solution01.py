# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        resultS = func(s)
        logger("resultS=%s" % resultS)

        result = convertFunc(resultS)

        logger("result=%s" % result)
        return result
        pass


def func(s: str) -> str:

    logger("input=%s" % s)
    leftP = -1
    rightP = -1
    for idx, value in enumerate(s):

        if value == ")":
            if leftP == -1:
                continue
            else:
                rightP = idx
                part1 = s[:leftP]
                part2 = s[leftP + 1 : rightP]
                part3 = s[rightP + 1 :]
                newS = part1 + "0" + part2 + "1" + part3
                logger("part1=%s, part2=%s, part3=%s" % (part1, part2, part3))
                logger("newS=%s" % newS)
                return func(newS)

        if value == "(":
            leftP = idx
            continue

    return s


def convertFunc(s: str) -> str:

    newS = ""

    for c in s:

        if c == "0":
            newS += "("
            continue

        if c == "1":
            newS += ")"
            continue

        if c == "(" or c == ")":
            continue

        newS += c

    return newS
