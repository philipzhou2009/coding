# https://leetcode.com/problems/trapping-rain-water/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def trap(self, height: List[int]) -> int:

        result = getResult(height)
        logger("result=", result)
        
        return result


def getResult(height: List[int]) -> int:

    logger("input=", height)

    nHeight = len(height)

    zeroFlag = True
    for i in height:
        if i != 0:
            zeroFlag = False
            break

    if zeroFlag:
        return 0

    tmpHeight = []
    head = None
    tail = None
    nextHeight = []
    for idx, i in enumerate(height):
        h = 1 if i > 0 else 0
        tmpHeight.append(h)

        if h > 0:
            if head == None:
                head = idx
            tail = idx

        nextHeight.append(i - 1 if i > 1 else 0)

    counter = 0
    for i in range(head, tail + 1):
        if tmpHeight[i] == 0:
            counter = counter + 1

    logger(
        "tmpHeight=",
        tmpHeight,
        "head=",
        head,
        "tail=",
        tail,
        "counter=",
        counter,
        "nextHeight=",
        nextHeight,
    )

    nextCounter = getResult(nextHeight)

    logger("nextCounter=", nextCounter)

    result = counter + nextCounter

    return result


# getResult([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

