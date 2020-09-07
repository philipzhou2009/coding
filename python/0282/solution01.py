#

from typing import List
import math
import itertools

logger = print if False else lambda *arg: None


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        nLen = len(num)
        result = []
        partial = func(num, target)
        result += partial
        for w in range(2, nLen):
            logger("w=", w)
            partial = func2(num, target, w)
            result += partial

        logger("result=", result)
        return result


def func(num: str, target: int) -> List[str]:
    nLen = len(num)
    productObj = itertools.product("+-*", repeat=(nLen - 1))
    pList = list(productObj)
    logger("pList=", pList)

    result = []
    for v in pList:
        idx = 0
        newS = ""
        while idx < nLen - 1:
            newS += num[idx] + v[idx]
            idx += 1
        newS += num[-1]

        ev = eval(newS)
        logger("newS=%s, ev=%s" % (newS, ev))
        if ev == target:
            result.append(newS)
        pass

    return result


def func2(num: str, target: int, w: int) -> List[str]:

    nLen = len(num)
    productObj = itertools.product("+-*", repeat=(nLen - w))
    pList = list(productObj)
    logger("pList=", pList)

    tmpList = []
    cursor = 0
    while cursor < nLen - w + 1:
        list1 = []
        for i in range(cursor):
            list1.append(num[i])
            pass
        list1.append(num[cursor : cursor + w])

        for i in range(cursor + w, nLen):
            list1.append(num[i])

        tmpList.append(list1)
        cursor += 1
        pass

    logger("tmpList=", tmpList)

    result = []
    for v in pList:
        for i in tmpList:
            idx = 0
            newS = ""
            while idx < len(i) - 1:
                newS += i[idx] + v[idx]
                idx += 1
            newS += i[-1]

            try:
                ev = eval(newS)
                logger("newS=%s, ev=%s" % (newS, ev))
                if ev == target:
                    result.append(newS)
            except:
                logger("eval error for ", newS)
        pass
    return result
