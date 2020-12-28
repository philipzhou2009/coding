# https://leetcode.com/problems/count-the-number-of-consistent-strings/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        result = 0
        for word in words:

            sortedChars = sorted(word)

            lastChar = None
            newWord = ""
            for c in sortedChars:

                if lastChar == None or lastChar != c:
                    lastChar = c
                    newWord = newWord + c
                pass
            logger("newWord=", newWord)

            if newWord == allowed:
                result = result + 1
            pass

        return result
