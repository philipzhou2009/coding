# https://leetcode.com/problems/non-overlapping-intervals/
# https://leetcode.com/problems/non-overlapping-intervals/discuss/778878/Python-Greedy-Solution-with-Explanation
from typing import List

def emptyFunc(*args):
    pass


enableLog = True
logger = print if enableLog else emptyFunc

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        # logger(intervals)
        end = float('-inf')

        count = 0

        for p1, p2 in intervals:
            if p1 < end:
                logger(p1, p2)
                count += 1
                continue
            
            end = max(end, p2)
        
        return count