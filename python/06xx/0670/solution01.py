# https://leetcode.com/problems/maximum-swap/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def maximumSwap(self, num: int) -> int:

        tmp = num
        tmpStr = str(num)

        logger("tmpStr=%s" % tmpStr)

        list1 = list(tmpStr)
        list1.sort(reverse=True)
        logger("list1=", list1)

        idx1 = -1
        for idx, value in enumerate(tmpStr):
            if value < list1[0]:
                idx1 = idx
                value1 = value
                break

        if idx1 == -1:
            result = num

        nextMax = list1[-1]
        nextMaxIdx = -1
        for idx, value in enumerate(tmpStr[idx1 + 1 :]):
            if value > nextMax:
                nextMax = value
                nextMaxIdx = idx

        logger("nextMax=%s, nextMaxIdx=%s" % (nextMax, nextMaxIdx))

        # tmpValue = tmpStr[nextMaxIdx]
        # tmpStr[nextMaxIdx] = value
        # tmpStr[idx1] = tmp

        logger("tmpStr=%s" % tmpStr)

        # while tmp > 0:
        #     i = tmp % 10

        pass
