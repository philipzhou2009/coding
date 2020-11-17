# https://leetcode.com/problems/sort-colors/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        logger("input=", nums)
        myOwnSort1(nums, len(nums))
        logger("result=", nums)


def myOwnSort1(nums: List[int], end: int) -> None:
    cursor = 0
    nLen = len(nums)
    while True:
        if cursor + 1 >= end:
            break

        first = nums[cursor]
        second = nums[cursor + 1]

        if first > second:
            nums[cursor + 1] = first
            nums[cursor] = second

        cursor = cursor + 1
        pass

    logger("nums=", nums)

    if end > 0:
        myOwnSort1(nums, end - 1)
    pass


# def myOwnSort(nums: List[int]) -> None:
#     cursor = 0
#     nLen = len(nums)
#     while True:
#         if cursor + 1 >= nLen:
#             break

#         first = nums[cursor]
#         second = nums[cursor + 1]

#         if first > second:
#             nums[cursor + 1] = first
#             nums[cursor] = second

#         cursor = cursor + 1
#         pass

#     logger("nums=", nums)

#     if len(nums[0:-1]) > 0:
#         myOwnSort(nums[0:-1])
#     pass


# myOwnSort1([2, 0, 2, 1, 1, 0], 6)
