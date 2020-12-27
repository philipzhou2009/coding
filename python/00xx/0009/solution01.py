# https://leetcode.com/problems/palindrome-number/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        sTmp = str(x)
        logger("sTmp=", sTmp)

        sLen = len(sTmp)

        result = True
        for i in range(int(sLen / 2)):
            logger(i)
            if sTmp[i] != sTmp[sLen - 1 - i]:
                result = False
                break

        return result
