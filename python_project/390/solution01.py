# https://leetcode.com/problems/elimination-game/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def lastRemaining(self, n: int) -> int:

        if n == 1:
            return 1

        list2 = []
        i = 1
        while i < n+1:
            list2.append(1)
            i += 1

        # logger(list2)
        reversed = False
        counter = 0
        while True:
            lastIdx = findForwardNext(list2, -1)
            list2[lastIdx] = 0
            counter += 1
            if counter == n - 1:
                break
            while True:
                idx1 = findForwardNext(list2, lastIdx)
                if idx1 == -1:
                    break

                idx2 = findForwardNext(list2, idx1)
                if idx2 == -1:
                    break

                list2[idx2] = 0
                counter += 1
                lastIdx = idx2

            logger("here: ", list2)

            if counter == n - 1:
                break
            else:
                list2.reverse()
                reversed = True if reversed == False else False

        logger("reversed=", reversed)
        if reversed:
            list2.reverse()

        logger(list2)

        i = 0
        for idx, e in enumerate(list2):
            if e == 1:
                i = idx
                break

        i += 1
        logger("i=", i)
        return i


def findForwardNext(list: List[int], start: int):
    i = 0
    for e in list:
        if i <= start:
            i += 1
            continue

        if e == 1:
            return i
            break

        i += 1
    return -1
