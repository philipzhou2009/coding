# https://leetcode.com/problems/count-the-number-of-consistent-strings/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        result = 0
        dict1 = {}
        lastBin = None
        for cInt in range(97, 97 + 26):

            if lastBin == None:
                lastBin = 1
            else:
                lastBin = lastBin << 1
            pass
            c1 = chr(cInt)
            # bin1 = bin(lastBin)
            logger("char=", c1, ",bin=", lastBin)
            dict1[c1] = lastBin

        logger("dict=", dict1)

        merged = 0
        for char in allowed:
            merged = merged | dict1[char]
            pass

        logger("merged=", merged)

        result = 0
        for word in words:

            if isConsistent(word, dict1, merged) == True:
                result += 1
            pass

        return result


def isConsistent(word: str, dict1, compare: int) -> bool:

    merged = 0
    for char in word:

        merged = merged | dict1[char]
        pass

    if merged &  compare == merged:
        return True

    return False
