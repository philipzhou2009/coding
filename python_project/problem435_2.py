# https://leetcode.com/problems/non-overlapping-intervals/
from typing import List


def emptyFunc(*args):
    pass


enableLog = True
logger = print if enableLog else emptyFunc
counter = 0


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        global counter
        totalLen = len(intervals)
        if totalLen == 0:
            return 0

        intervals.sort(key=intervalSort)
        logger("sorted intervals=", intervals)
        logger("totalLen=", totalLen)
        # return 1

        findProperNoOverLaps(intervals, 1)

        return 0


def findProperNoOverLaps(intervals: List[List[int]], steps: int):
    global counter
    counter += 1
    if counter > 10:
        return


    print(intervals, steps)

    if len(intervals) <= 1:
        return steps

    firstOne = intervals[0]
    tmpIntervals = []

    for ce in intervals[1:]:
        if firstOne[1] <= ce[0]:
            tmpIntervals.append(ce)

    if len(tmpIntervals) == 0:
        return steps
    # print(firstOne, ":", tmpIntervals)

    i = 0
    max = 0
    for ce in tmpIntervals:
        newSteps = findProperNoOverLaps(tmpIntervals[i:], steps+1)
        print("newSteps=", newSteps)
        if newSteps > max:
            max = newSteps

        i += 1

        pass

    return max
    pass


def intervalSort(e):
    return e[0]


def newFunc(intervals: List[List[int]]):
    lenIntervals = len(intervals)
    logger("input intervals=", intervals)
    logger("input length=", lenIntervals)
    lastOne = intervals[0]
    i = 0
    flag = False

    for ce in intervals[1:]:
        i += 1
        if lastOne[1] <= ce[0]:
            lastOne = ce
            continue
        else:
            # overlap
            flag = True
            break
        pass

    if flag == True:
        cursorList1 = i+1
        while True:
            if cursorList1 > lenIntervals-1:
                break
            if intervals[i-1][1] <= intervals[cursorList1][0]:
                break
            else:
                # overlap
                cursorList1 += 1
            pass

        cursorList2 = i+1
        while True:
            if cursorList2 > lenIntervals - 1:
                break
            if intervals[i][1] <= intervals[cursorList2][0]:
                break
            else:
                cursorList2 += 1
            pass

        logger("cursorList1=", cursorList1)
        logger("cursorList2=", cursorList2)
        list1 = []
        list1.extend(intervals[0: i])
        if cursorList1 < lenIntervals:
            list1.extend(intervals[cursorList1:])

        list2 = []
        list2.extend(intervals[: i-1])
        list2.extend(intervals[i:i+1])
        if cursorList2 < lenIntervals:
            list2.extend(intervals[cursorList2:])

        if True:
            lenList1 = newFunc(list1)
            lenList2 = newFunc(list2)
            return lenList1 if lenList1 > lenList2 else lenList2
        else:
            return 0
    else:
        theLen = len(intervals)
        if theLen > 6:
            print(intervals)
        logger("found length", theLen)
        return theLen
