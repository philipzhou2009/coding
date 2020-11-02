from typing import List

# https://leetcode.com/problems/permutation-in-string/

logger = print if False else lambda *arg: None


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s2Len = len(s2)
        s1Len = len(s1)

        s1Dict = {}
        for e in s1:
            if e in s1Dict:
                s1Dict[e] += 1
            else:
                s1Dict[e] = 1
            pass

        logger("s1Dic=%s" % s1Dict)

        newDict = {}
        cursor1 = cursor = 0

        while cursor1 < s2Len:
            flag = 0
            subStr = s2[cursor : cursor + s1Len]
            logger("subStr=%s" % subStr)
            for i in subStr:
                if not i in s1Dict:
                    flag = 1
                    cursor += 1
                    cursor1 = cursor
                    break

                if i in newDict:
                    newDict[i] += 1
                else:
                    newDict[i] = 1

                cursor += 1

            if flag == 1:
                newDict = {}
                continue

            logger("newDict=%s" % newDict)    
            if newDict == s1Dict:
                return True

            cursor1 += 1
            cursor = cursor1
            newDict = {}

            pass

        return False
