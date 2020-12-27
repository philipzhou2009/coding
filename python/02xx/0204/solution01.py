# https://leetcode.com/problems/count-primes/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2:
            return 0

        primeList = []
        result = 1
        for i in range(3, n, 2):
            bTmp = isPrime(i, primeList)
            # logger("i=%s, b=%s" % (i, bTmp))
            if bTmp == True:
                primeList.append(i)
                result = result + 1

        return result


def isPrime(n: int, primeList: List[int]) -> bool:
    # logger("primeList=", primeList)

    half = int(n / 2)
    result = True
    for i in primeList:
        if n % i == 0:
            result = False
            break

        if i > half:
            break
        pass

    return result