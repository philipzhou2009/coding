# https://leetcode.com/problems/task-scheduler/

from typing import List
from collections import Counter

logger = print if True else lambda *arg: None


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maximum = max(counter.values())
        maxTask = 0
        for i in counter:
            if counter[i] == maximum:
                maxTask += 1
        return max(((maximum - 1) * (n + 1) + maxTask), len(tasks))

