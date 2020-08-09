# https://leetcode.com/problems/elimination-game/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def lastRemaining(self, n: int) -> int:

        if n == 1:
            return 1
        if n < 5:
            return 2

        newN = n
        if n % 2 == 1:
            newN = n - 1

        nList = []
        for i in range(newN, 0, -2):
            nList.append(i)

        logger("nList", nList)

        newList = eliminate(nList)
        logger("here", newList)

        return newList[0]


def eliminate(list: List[int]):
    i = 0
    totalLen = len(list)
    while i < totalLen:
        list[i] = 0
        i += 2

    logger("after pop list", list)

    newList = []
    for e in list:
        if e != 0:
            newList.append(e)
        pass

    logger("newList", newList)

    if len(newList) > 1:
        newList.reverse()
        return eliminate(newList)
    else:
        return newList
