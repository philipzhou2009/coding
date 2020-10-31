# https://leetcode.com/problems/longest-well-performing-interval/

from typing import List

loggerFlag: bool = False
logger = print if loggerFlag else lambda *arg: None


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        list1 = []
        currentSet = set()
        sLen = len(s)

        for idx, c in enumerate(s):

            logger("c=", c)
            if not c in currentSet:
                currentSet.add(c)
            else:
                list1.append(currentSet)
                currentSet = set()
                currentSet.add(c)

            if idx == sLen - 1:
                list1.append(currentSet)

        logger("list1=", list1)

        result = 0
        for tmpSet in list1:
            result = len(tmpSet) if len(tmpSet) > result else result
            pass

        return result
