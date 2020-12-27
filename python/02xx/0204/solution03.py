# https://leetcode.com/problems/count-primes/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2:
            return 0

        iSet = set()
        for i in range(2, n):
            k = int(n / i) + 1
            if i > k:
                break

            iTmp = None
            for j in range(i, k):
                if iTmp == None:
                    iTmp = j * i
                else:
                    iTmp = iTmp + i

                logger("%s %s %s" % (i, j, iTmp))

                if iTmp < n:
                    iSet.add(iTmp)
                pass

            pass

        logger("prime set=", iSet)

        result = n - 2 - len(iSet)
        return result
