# https://leetcode.com/problems/coin-change/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        tmp = getCoins(coins, amount)

        return -1 if tmp == "inf" else tmp
        # pass


def getCoins(coins: List[int], amount: int):

    maxDeno = coins[0]
    cLen = len(coins)

    if amount == 0:
        return 0

    if cLen == 1:
        if not amount % maxDeno == 0:
            return float("inf")
        else:
            tmp = int(amount / maxDeno)
            logger(tmp)
            return tmp

    coinCount = int(amount / maxDeno)
    logger("coins with maxDeno=", coinCount)

    result = float("inf")
    for i in range(coinCount + 1):

        # getCoins(coins[1:], amount - maxDeno * i)
        tmpCoins = getCoins(coins[1:], amount - maxDeno * i)
        logger("tmpCoins=", tmpCoins)
        tmpResult = i + tmpCoins
        result = tmpResult if tmpResult < result else result

        pass

    logger("coins=", coins, ", amount=", amount, ", result=", result)
    return result


# getCoins([5, 2, 1], 11)
# getCoins([5, 5, 2, 1], 10)
