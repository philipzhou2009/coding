# https://leetcode.com/problems/count-primes/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2:
            return 0

        iSet = set()
        for i in range(2, n):

            k = int(n / i) + 1

            for j in range(i, k):
                iTmp = j * i

                logger("%s %s %s" % (i, j, iTmp))

                if iTmp < n:
                    iSet.add(iTmp)
                pass

            pass

        logger("prime set=", iSet)

        result = n - 2 - len(iSet)
        return result
