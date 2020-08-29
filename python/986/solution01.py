# https://leetcode.com/problems/interval-list-intersections/

from typing import List

logger = print if True else lambda *arg: None


def myFunc(input: List[int]):
    return input[1]


class Solution:
    def intervalIntersection(
        self, A: List[List[int]], B: List[List[int]]
    ) -> List[List[int]]:

        logger("A=", A)
        logger("B=", B)

        newList = A + B

        newList.sort(key=myFunc)
        newListLen = len(newList)
        logger("newList=", newList)

        anotherList = newList
        while True:
            cursor = 0
            tmpList = []
            flag = False
            while cursor < len(anotherList) - 1:

                eLeft = anotherList[cursor]
                eRight = anotherList[cursor + 1]
                logger(eLeft, eRight)

                if eLeft[1] >= eRight[0]:
                    flag = True
                    if eLeft[0] < eRight[0]:
                        overlap = [eRight[0], eLeft[1]]
                    else:
                        overlap = [eLeft[0], eLeft[1]]
                    
                    # logger("overlap=", overlap)
                    tmpList.append(overlap)

                cursor += 1
                continue

            if flag == False:
                break
            else:
                logger("tmpList=", tmpList)    
                anotherList = tmpList    


        logger("result=", anotherList)
        return anotherList
