# https://leetcode.com/problems/sum-of-square-numbers/

from typing import List
import math

verbose: bool = True
logger = print if verbose else lambda *arg: None


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        logger("c=", c)

        list1 = []
        cHalf = int(c / 2)
        for i in range(cHalf + 1):
            logger("i=", i)
            list1.append((i, c - i))
            pass

        logger("list1=", list1)

        resultB = False

        for t in list1:
            logger("t=", t)

            root1 = math.sqrt(t[0])
            result1 = True if root1 - int(root1) == 0 else False

            if not result1:
                continue

            root2 = math.sqrt(t[1])
            result2 = True if root2 - int(root2) == 0 else False
            if not result2:
                continue

            logger("result1=%s,result2=%s" % (result1, result2))

            if result1 and result2:
                resultB = True
                break

            pass

        return resultB
