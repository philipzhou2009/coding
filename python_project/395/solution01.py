# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

logger = print if False else lambda *arg: None


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        sLen = len(s)
        i = 0
        maxLen = 0
        while i < sLen:
            newStr = s[i:]
            if sLen - i < maxLen:
                break
            newLen = func(newStr, k)

            maxLen = newLen if newLen > maxLen else maxLen
            logger("maxLen", maxLen)
            i += 1

        logger("result max len=", maxLen)

        return maxLen


def isValid(theDict: dict, k: int):

    for x, y in theDict.items():
        if y < k:
            return False

    return True


def func(s: str, k: int):
    logger("input str=", s)
    theDict = {}
    counter = 0
    nEnd = -1
    theLen = 0
    for e in s:
        counter += 1
        # logger("e=", e)

        if e in theDict:
            theDict[e] += 1
        else:
            theDict[e] = 1

        logger("theDict=", theDict)
        valid = isValid(theDict, k)

        if valid and counter > nEnd:
            theLen = counter

    return theLen

