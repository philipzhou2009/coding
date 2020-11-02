# https://leetcode.com/problems/bitwise-and-of-numbers-range/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        logger("m=%s, n=%s" % (m, n))

        if m == n:
            return m

        if n < 2:
            return 0

        tmp1 = 1
        tmp2 = 2
        while True:
            if tmp1 <= m:
                tmp1 *= 2
                tmp2 *= 2
                continue

            if tmp1 > m and tmp1 < n:
                logger("here1 tmp1=%s, tmp2=%s" % (tmp1, tmp2))
                return 0
                # if tmp2 <= n:
                #     return 0
                # else:
                #     logger("here2 tmp1=%s, tmp2=%s" % (tmp1, tmp2))
                #     return tmp1
            elif tmp1 == m:
                return tmp1
            elif tmp1 == n:
                logger("here3 tmp1=%s, tmp2=%s" % (tmp1, tmp2))
                return 0
            else:
                logger("here4 tmp1=%s, tmp2=%s" % (tmp1, tmp2))
                return int(tmp1 / 2)

        pass
