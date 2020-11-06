# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        d1 = {}

        for idx, i in enumerate(nums):
            tmp = d1.get(i)
            if not tmp == None:
                d1[i] = tmp + 1
            else:
                d1[i] = 1

        logger("d1=", d1)

        result = []
        for i in d1:

            if not d1[i] == 1:
                result.append(i)
            pass

        return result
