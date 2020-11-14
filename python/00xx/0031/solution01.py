# https://leetcode.com/problems/next-permutation/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nLen = len(nums)
        # position = None
        flag = True

        for idx in range(nLen-1, -1, -1):
            logger("idx=", idx)

            if idx -1 < 0:
                flag = False
                break

            v1 = nums[idx]
            v2 = nums[idx-1]
            if v1 > v2:
                flag = True
                # tmp = v1
                nums[idx] = v2
                nums[idx-1] = v1
                break

        if flag == False:
            nums.sort()        

        pass
