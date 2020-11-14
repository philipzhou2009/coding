# https://leetcode.com/problems/decode-ways/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def numDecodings(self, s: str) -> int:
        set1 = set()
        counter = func(s, set1)

        logger("counter=", counter)
        return counter


def func(sInput: str, set1: set) -> int:
    s = sInput

    if len(s) == 1:
        s1 = s[0]
        logger("s1=", s1)
        is1 = int(s1)
        if is1 > 0 and is1 < 27:
            logger("here1")
            return 1
        return 0

    if len(s) == 2:
        s2 = s[0:2]
        logger("s2=", s2)
        is2 = int(s2)
        if s2[0] == "0" or is2 in set1:
            return 0
        if is2 > 0 and is2 < 27:
            logger("here2")
            set1.add(is2)
            return 1 + func(s[1:], set1)

    return func(s[1:], set1) + func(s[2:], set1)

