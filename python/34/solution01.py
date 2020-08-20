# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        result = func(nums, target, 0)
        logger("result=%s" % result)
        return result
        pass


def func(nums: List[int], target: int, travel: int) -> List[int]:

    nLen = len(nums)

    if nLen == 0:
        return [-1, -1]

    if nLen == 1:
        if nums[0] == target:
            return [0 + travel, 0 + travel]
        else:
            return [-1, -1]

    nHalf = int(nLen / 2)

    logger("nHalf=%s" % nHalf)

    if nums[nHalf - 1] > target:
        return func(nums[0:nHalf], target, travel)
    elif nums[nHalf - 1] < target:
        return func(nums[nHalf:], target, travel + nHalf)
    else:
        # found it
        cursorLeft = cursorRight = nHalf - 1
        while cursorLeft > -1:
            if nums[cursorLeft] == target:
                cursorLeft -= 1
            else:
                break

        while cursorRight < nLen:
            if nums[cursorRight] == target:
                cursorRight += 1
            else:
                break

        logger("left=%s,right=%s,travel=%s" % (cursorLeft + 1, cursorRight - 1, travel))
        return [cursorLeft + travel + 1, cursorRight + travel - 1]

    pass
