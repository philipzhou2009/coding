# https://leetcode.com/problems/basic-calculator-ii/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def calculate(self, s: str) -> int:

        sLen = len(s)

        theList = []
        lastIdx = 0
        for i, v in enumerate(s):

            if not v.isdigit() and not v == " ":
                theList.append(int(s[lastIdx:i].strip()))
                theList.append(v)
                lastIdx = i + 1

        theList.append(int(s[lastIdx:].strip()))

        logger("theList=", theList)

        tmpList = theList
        list1 = []
        j = 1
        while j < len(theList):
            jv = tmpList[j]

            if jv == "*" or jv == "/":
                tmpV = (
                    tmpList[j - 1] * tmpList[j + 1]
                    if jv == "*"
                    else (tmpList[j - 1] / tmpList[j + 1])
                )
                list1.append(int(tmpV))
                j += 2
                continue
            elif jv == "+" or jv == "-":
                list1.append(tmpList[j - 1])
                list1.append(jv)

            if j == sLen - 1:
                list1.append(tmpList[j])
            j += 1

        logger("list1=", list1)

        k = 1
        last = list1[0]
        while k < len(list1):

            kv = list1[k]
            if kv == "+" or kv == "-":
                last = last + list1[k + 1] if kv == "+" else (last - list1[k - 1])

            k += 1

        logger("last=", last)

        return last


# solution=Solution()
# solution.calculate("3+2*2")
# solution.calculate(" 3/2 ")
# solution.calculate(" 3+5 / 2 ")
