# https://leetcode.com/problems/total-hamming-distance/

from typing import List

from collections import Counter

logger = print if False else lambda *arg: None


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

    counter = Counter()
    binStr = "{0:b}".format(input)
    for c in binStr:

        counter[c] += 1
        pass

    logger("counter=%s" % counter)
    return counter["1"]
