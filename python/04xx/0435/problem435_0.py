# https://leetcode.com/problems/non-overlapping-intervals/
from typing import List


def emptyFunc(*args):
    pass


logger = print if True else emptyFunc
counter = 0


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        totalLen = len(intervals)
        if totalLen == 0:
            return 0

        intervals.sort(key=intervalSort)
        logger("sorted intervals:", intervals)
        logger("len:", totalLen)
        # return 1

        resultLen = newFunc(intervals)
        logger("resultLen", resultLen)

        eraseLen = totalLen - resultLen
        logger("eraseLen", eraseLen)
        return eraseLen


def intervalSort(e):
    return e[0]


def newFunc(intervals: List[List[int]]):
    # global counter
    # counter += 1
    # if counter > 10:
    #     return 0

    lastOne = intervals[0]
    i = 0
    flag = False

    for ce in intervals[1:]:
        i += 1
        leftValue = ce[0]
        rightValue = ce[1]
        if lastOne[1] <= leftValue:
            lastOne = ce
            continue
        else:
            # overlap
            flag = True
            break
        pass

    if flag == True:
        list1 = []
        list1.extend(intervals[0: i])
        list1.extend(intervals[i+1:])
        list2 = []
        list2.extend(intervals[: i-1])
        list2.extend(intervals[i:])

        logger("list1", list1)
        logger("list2", list2)

        lenList1 = newFunc(list1)
        lenList2 = newFunc(list2)

        logger("found length of list1", lenList1)
        logger("found length of list2", lenList2)

        return lenList1 if lenList1 > lenList2 else lenList2
        # return 0
    else:
        theLen = len(intervals)
        logger("found a length", theLen)
        return theLen
