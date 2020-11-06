# https://leetcode.com/problems/total-hamming-distance/

# this solution(solution04) similar to the one here, but I did not manage find the better implementation
# https://leetcode.com/problems/total-hamming-distance/discuss/770198/Python-O(N)-solution-with-explanation


from typing import List

from collections import Counter

logger = print if False else lambda *arg: None


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        result = 0
        nLen = len(nums)
        dict1 = {}
        list1 = []

        nums.sort(reverse=True)
        logger("nums=%s" % nums)

        for i in nums:
            binStr = toBinStr(i)
            list1.append(binStr)
            pass

        logger(list1)

        for idx1, str1 in enumerate(list1):

            cursor = 0
            logger("str1=%s" % str1)
            while cursor < len(str1):
                c = str1[cursor]
                logger("c=%s" % c)

                tmpResult = 0
                idx2 = idx1 + 1
                while idx2 < nLen:
                    str2 = list1[idx2]
                    logger("str2=%s" % str2)
                    idx2 += 1

                    if cursor >= len(str2):
                        tmpResult += 1
                        continue

                    if cursor < len(str2) and str2[cursor] != c:
                        tmpResult += 1

                logger("tmpResult=%s" % tmpResult)
                cursor += 1
                result += tmpResult

            pass

        logger("result=%s" % result)
        return result


def toBinStr(input: int) -> str:

    str1 = bin(input)
    str2 = str1[2:][::-1]

    # logger("str2=%s" % str2)
    return str2


def func(input: int) -> List[int]:

    i = input
    cursor = 0
    result0 = []
    result = set()
    while i != 0:
        if i % 2 == 1:
            result.add(cursor)
            i -= 1
        else:
            i /= 2
            cursor += 1

    logger(result)
    return result
