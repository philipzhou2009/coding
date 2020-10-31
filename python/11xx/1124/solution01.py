# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import List

loggerFlag: bool = True
logger = print if loggerFlag else lambda *arg: None


class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        tmpList = []
        tiring = 0
        nonTiring = 0

        j = k = 0
        tiringFlag = hours[0] > 8

        tmpList.append(0)

        # for idx, i in enumerate(hours):
        #     logger("i=", i)

        #     tmpB = i > 8
        #     if tmpB == tiringFlag:
        #         continue

        #     else:
        #         tmpList.append(idx)
        #         tiringFlag = tmpB

        #     pass
        # logger("index list=", tmpList)

        list1 = []
        tmpSum = 0
        hoursLen = len(hours)
        for idx, i in enumerate(hours):
            logger("i=", i)
            tmpB = i > 8
            if tmpB == tiringFlag:
                tmpSum = tmpSum + 1
            else:
                list1.append(tmpSum)
                tmpSum = 1
                tiringFlag = tmpB
                if idx == hoursLen - 1:
                    list1.append(tmpSum)

        logger("list1=", list1)


        



        pass

