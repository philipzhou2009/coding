# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        resultList = func0(s)
        resultLen = len(resultList)

        newS = ""

        if resultLen == 0:
            newS = s
        else:
            idx = 0
            lastIdx = resultList[0][0]
            newS += s[0:lastIdx]

            for idx in range(1, resultLen, 1):
                e = resultList[idx]
                # logger("str in between=%s" % s[lastIdx + 1 : e[0]])
                newS += s[lastIdx + 1 : e[0]]
                lastIdx = e[0]

            newS += s[resultList[resultLen - 1][0] + 1 :]

        logger("result=%s" % newS)
        return newS


def func0(s: str) -> str:

    # logger("input=%s" % s)
    list1 = []
    for idx, c in enumerate(s):
        if c == "(" or c == ")":
            list1.append((idx, c))
        pass

    idx = 0
    flag = True

    while True:
        logger("list1=", list1)
        idx = 0
        flag = False
        leftP = -1
        rightP = -1

        while True:
            if idx >= len(list1):
                break
            e = list1[idx]
            if e[1] == ")":
                if leftP == -1:
                    idx += 1
                    continue
                else:
                    rightP = idx
                    # logger("leftP=%s, rightP=%s" % (leftP, rightP))
                    list1.pop(leftP)
                    list1.pop(rightP - 1)
                    flag = True
                    break
            if e[1] == "(":
                leftP = idx
                idx += 1
                continue

        if flag == False:
            # nothing to do
            break

    # logger("list1=", list1)

    return list1
