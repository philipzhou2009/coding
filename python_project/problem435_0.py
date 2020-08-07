# https://leetcode.com/problems/non-overlapping-intervals/
from typing import List


def intervalSort(e):
    return e[0]


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=intervalSort)
        print(intervals)

        resultList = []

        skips = []
        skipsLen = 0

        counter = 0
        while True:
            lastOne = firstOne = intervals[0]
            result = [firstOne]
            i = 0
            flag = False
            for interval in intervals[1:]:
                i += 1

                print("interval", interval)
                try:
                    skips.index(i)
                    print("skip", i)
                    continue
                except:
                    pass     

                # overlap
                if interval[0] >= lastOne[1]:
                    result.append(interval)
                    lastOne = interval
                elif flag == False:
                    skips.append(i-1)
                    flag = True

            print("skips", skips)        
            print("result", result)
            print("===============")
            
            newLen = len(skips)
            if newLen == skipsLen:
                break
            else:
                skipsLen = newLen
            counter += 1
            if counter == 5:
                break
            # break

        # print(resultList)

        return 1
