# https://leetcode.com/problems/reach-a-number/

from typing import List

loggerFlag: bool = True
logger = print if loggerFlag else lambda *arg: None


class Solution:
    def reachNumber(self, target: int) -> int:

        i = 1
        sum = 0
        found = False

        if target == 0:
            return 0

        newTarget = target if target > 0 else target * -1

        while True:
            sum = sum + i
            # step = step + 1
            logger("sum=%s, i=%s" % (sum, i))

            if sum == newTarget:
                found = True
            elif sum > newTarget:
                gap = sum - newTarget
                logger("gap=%s" % gap)
                for c in range(i + 1):
                    # logger("gap=%s, c=%s" % (gap, c))
                    if gap == 2 * c:
                        found = True
                        break
                    pass

            if found:
                break

            i = i + 1
            pass

        logger("i=%s" % i)

        return i

