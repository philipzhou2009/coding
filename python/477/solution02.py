# https://leetcode.com/problems/total-hamming-distance/

from typing import List

from collections import Counter

logger = print if True else lambda *arg: None


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        result = 0
        nLen = len(nums)

        for idx1, i in enumerate(nums):
            logger("idx=%s, value=%s" % (idx1, i))
            idx2 = idx1 + 1
            while idx2 < nLen:
                j = nums[idx2]
                k = i ^ j
                idx2 += 1

                logger("i=%s, j=%s, k=%s" % (i, j, k))
                result += getOnes(k)

        return result


def getOnes(input: int) -> int:

    i = input
    counter = 0
    while i != 0:
        tmp = i % 2
        if tmp == 1:
            i -= 1
            counter += 1
        else:
            i = i / 2

    logger("counter=%s" % counter)

    return counter


def getOnes0(input: int) -> int:

    counter = Counter()
    binStr = "{0:b}".format(input)
    for c in binStr:

        counter[c] += 1
        pass

    logger("counter=%s" % counter)
    return counter["1"]
