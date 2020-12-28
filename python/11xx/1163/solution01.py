# https://leetcode.com/problems/last-substring-in-lexicographical-order/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def lastSubstring(self, s: str) -> str:

        result = getResult(s)

        logger("result=", result)
        return result


def getResult(s: str) -> str:

    maxChar = "a"
    charDict = {}
    for idx, i in enumerate(s):
        maxChar = i if i > maxChar else maxChar

        if charDict.get(i) == None:
            charDict[i] = [idx]
        else:
            charDict[i].append(idx)

    logger("charDict=", charDict, "maxChar=", maxChar)

    pos = charDict[maxChar]
    maxStr = ""
    for idx, i in enumerate(pos):
        tmpStr = s[i:]
        logger("tmpStr=", tmpStr)
        maxStr = tmpStr if tmpStr > maxStr else maxStr
        pass

    return maxStr


# getResult("leetcode")
