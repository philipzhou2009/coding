# https://leetcode.com/problems/longest-well-performing-interval/

from typing import List

loggerFlag: bool = False
logger = print if loggerFlag else lambda *arg: None


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sLen = len(s)

        result = 0
        for i in range(sLen):

            tmpS = s[i:]
            logger("tmpS=", tmpS)
            tmpLen = func(tmpS)
            result = tmpLen if tmpLen > result else result

        return result


def func(s: str) -> int:

    tmpList = []
    for idx, c in enumerate(s):

        if c in tmpList:
            break

        else:
            tmpList.append(c)

    logger("tmpList=", tmpList)

    return len(tmpList)

