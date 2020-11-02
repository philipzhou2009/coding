# https://leetcode.com/problems/elimination-game/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def lastRemaining(self, n: int) -> int:

        if n == 1:
            return 1

        newN = n
        if n % 2 == 1:
            newN = n - 1
            
        nList = []
        for i in range(newN, 0, -2):
            nList.append(i)

        logger("nList", nList)

        eliminate(nList)
        logger("here", nList)


        return nList[0]


def eliminate(list: List[int]):
    i = 0

    while i < len(list):
        list.pop(i)
        i += 1

    logger("after pop list", list)

    if len(list) > 1:
        list.reverse()
        eliminate(list)
