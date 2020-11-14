# https://leetcode.com/problems/word-search/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        pass


def func(
    board: List[List[str]], word: str, points: List, start: int
) -> bool:

    for ir, row in enumerate(board):
        logger("\n")
        for ic, i in enumerate(row):
            logger("i=", i)
    
    return False


subject = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
func(subject, "ABCCED", [], 0)
