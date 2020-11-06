# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

from typing import List

logger = print if False else lambda *arg: None

# deeedbbcccbdaa
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        result = func(s, k)
        logger("result=%s" % result)
        return result


def func(s: str, k: int) -> str:

    cursor2 = cursor1 = -1
    lastC = s[cursor1]
    counter = 0

    for idx, e in enumerate(s):
        # logger("idx=%s, e=%s" % (idx, e))
        if idx == -1:
            lastC = e
            counter += 1
            cursor1 = idx
            continue

        if lastC == e:
            counter += 1
        else:
            lastC = e
            counter = 1
            cursor1 = idx

        if counter == k:
            cursor2 = idx
            logger("found=%s, start=%s, end=%s" % (lastC, cursor1, cursor2))
            break

    if not cursor1 == -1 and not cursor2 == -1:
        newStr = s[0:cursor1] + s[cursor2 + 1 :]
        logger("newStr=%s" % newStr)
        return func(newStr, k)

    return s

