# https://leetcode.com/problems/sum-of-square-numbers/

from typing import List
import math

verbose: bool = False
logger = print if verbose else lambda *arg: None


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        logger("c=", c)

        j = int(math.sqrt(c)) + 1

        resultB = False

        for i in range(j):
            logger("i=", i)

            tmp1 = c - i * i
            root1 = math.sqrt(tmp1)
            logger("root=", root1)
            result1 = True if root1 - int(root1) == 0 else False

            if result1:
                resultB = True
                break

        return resultB

