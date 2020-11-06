# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        sLen = len(s)
        pLen = len(p)
        newP = "".join(sorted(p))
        logger("newP=%s" % newP)
        counter = 0
        result = []
        while counter < (sLen - pLen + 1):

            logger(counter)
            subStr = s[counter : (counter + pLen)]
            subStrSorted = sorted(subStr)
            newSub = "".join(subStrSorted)
            logger("sub=%s, sorted=%s" % (subStr, newSub))
            if newSub == newP:
                result.append(counter)
            counter += 1

        logger("result=", result)
        return result
