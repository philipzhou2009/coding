# https://leetcode.com/problems/trapping-rain-water/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def trap(self, height: List[int]) -> int:

        result = getResult(height)
        logger("result=", result)

        return result


def getResult(height: List[int]) -> int:

    head = None
    tail = None
    nHeight = len(height)

    for idx, i in enumerate(height):
        pass

    cursor = 0
    while True:
        tmpV = height[cursor]
        logger("tmpV=", tmpV)

        if tmpV != 0:
            if head == None:
                head = cursor

            if cursor >= nHeight - 1 or tmpV > height[cursor + 1]:
                tail = cursor
                break

        cursor = cursor + 1
        if cursor >= nHeight - 1:
            break

    logger("head=", head, "tail=", tail)

    return 0


getResult([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
