# https://leetcode.com/problems/palindromic-substrings/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def countSubstrings(self, s: str) -> int:
        result = func(s)
        return len(result)


def func(s: str):
    nLen = len(s)
    resultList = []
    for i in range(nLen):
        tmpLen = i + 1
        # logger("tmpLen=", tmpLen)
        cursor = 0
        while True:
            newStr = s[cursor : cursor + tmpLen]
            logger("newStr=", newStr)

            if isPalindromic(newStr):
                resultList.append(newStr)

            cursor = cursor + 1
            if cursor + tmpLen > nLen:
                break

    logger("resultList=", resultList)
    return resultList


def isPalindromic(s: str) -> bool:
    nLen = len(s)
    half = int(nLen / 2)
    logger("half=", half)

    result = True
    for i in range(half):
        # logger("i=", i)
        if not s[i] == s[nLen - i - 1]:
            result = False
            break

    logger("isPalindromic=", result)
    return result


# isPalindromic("aba")
# func("abcd")