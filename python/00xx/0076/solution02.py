# https://leetcode.com/problems/minimum-window-substring/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass


def getResult(s: str, t: str) -> str:

    d1 = {}
    for i in t:
        if d1.get(i) == None:
            d1[i] = 0

    logger("d1=", d1)

    pos = []
    newStr = ""
    for idx, i in  enumerate(s):
        if d1.get(i) == None:
            newStr = newStr + "X"

        else:
            newStr = newStr + i

            pos.append(idx)

    # logger("newStr=", newStr)
    logger("post=", pos)

    head = 0
    tail = None
    for i in pos:

        d1[s[i]] = d1[s[i]] +1

        

    pass


def getWindow(s: str, pos: List[int])-> int:

    pass

getResult("ADOBECODEBANC", "ABC")

