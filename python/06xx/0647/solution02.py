# https://leetcode.com/problems/palindromic-substrings/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def countSubstrings(self, s: str) -> int:
        result = func(s)
        return result

def func(s: str):
    nLen = len(s)
    # resultList = []
    counter  =0
    for i in range(nLen):
        tmpLen = i + 1
        # logger("tmpLen=", tmpLen)
        cursor = 0
        tmpList = []
        while True:
            newStr = s[cursor : cursor + tmpLen]
            logger("newStr=", newStr)

            if newStr in tmpList:
                counter = counter + 1
            elif isPalindromic(newStr):
                # resultList.append(newStr)
                tmpList.append(newStr)
                counter = counter + 1

            cursor = cursor + 1
            if cursor + tmpLen > nLen:
                break

        logger("tmpList=", tmpList)
        pass    

    # logger("resultList=", resultList)
    return counter


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

