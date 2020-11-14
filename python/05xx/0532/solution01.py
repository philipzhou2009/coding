# https://leetcode.com/problems/k-diff-pairs-in-an-array/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        pairs = getPairs(nums)
        counter = 0
        pairSet = set()
        # for pair in pairs:
        #     if abs(pair[0] - pair[1]) == k:
        #         if not pair in pairSet and not (pair[1], pair[0]) in pairSet:
        #             counter = counter + 1
        #             pairSet.add(pair)

        logger("counter=", counter)
        return counter


def getPairs(nums: List[int]) -> List:

    nLen = len(nums)
    result = []
    # for idx, i in enumerate(nums):
    for i in range(nLen - 1):
        # logger("=", i)
        cVal = nums[i]
        # logger("current=", cVal)

        for j in nums[i + 1 :]:
            # logger("j=", j)

            result.append((cVal, j))

        pass

    logger("result=", result)
    return result


# pairs([1, 2, 3, 4, 5], 1)

