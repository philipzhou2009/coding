# https://leetcode.com/problems/divide-two-integers/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:


        # logger("-2147483648/-1=%s" % (-2147483648 / -1))
        logger("2147483648 & 0x7FFFFFFF=%s" % (2147483648 and 0x7FFFFFFF))

        logger("input dividend=%s, divisor=%s" % (dividend, divisor))

        counter = 0
        e1 = e2 = 0

        flag = False
        tmpDivisor = divisor
        tmpDividend = dividend
        if dividend < 0 and divisor > 0:
            flag = True
            tmpDividend = tmpDividend - tmpDividend - tmpDividend

        if dividend > 0 and divisor < 0:
            flag = True
            tmpDivisor = tmpDivisor - tmpDivisor - tmpDivisor

        if dividend < 0 and divisor < 0:
            tmpDividend = tmpDividend - tmpDividend - tmpDividend
            tmpDivisor = tmpDivisor - tmpDivisor - tmpDivisor

        logger("input tmpDividend=%s, tmpDivisor=%s" % (tmpDividend, tmpDivisor))

        tmpResult = 0
        while True:

            e1 += tmpDivisor
            counter += 1
            if e1 == tmpDividend:
                tmpResult = counter
                break
            elif e1 < tmpDividend:
                continue
            else:
                tmpResult = counter - 1
                break

        logger("tmpResult=%s" % tmpResult)

        result = tmpResult
        if flag:
            result = tmpResult - tmpResult - tmpResult

        return result
