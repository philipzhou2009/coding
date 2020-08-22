# https://leetcode.com/problems/number-of-islands/

from typing import List

logger = print if False else lambda *arg: None


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        for e in grid:
            logger("%s" % e)
            pass

        # func(grid, (0, 0))

        round = 0
        while True:
            oneCoord = findOne(grid)
            if not oneCoord == ():
                logger("find One at (%s, %s)" % (oneCoord[0], oneCoord[1]))
                func(grid, oneCoord)
                round += 1
            else:
                break

        for e in grid:
            logger("%s" % e)
            pass

        return round
        pass


def findOne(grid: List[List[str]]) -> tuple:

    for y, listY in enumerate(grid):
        # logger("listY=", listY)
        for x, value in enumerate(listY):
            if value == "1":
                return (x, y)

    return ()


def func(grid: List[List[str]], coord: tuple) -> int:

    logger("input=", coord)

    x = coord[0]
    y = coord[1]

    theOne = grid[y][x]
    # logger("theOne=%s" % theOne)

    if theOne == "1":
        grid[y][x] = "X"

    width = len(grid[0])
    height = len(grid)
    # top, bottom, left, right coords
    list1 = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

    for e in list1:
        if e[0] >= 0 and e[0] < width and e[1] >= 0 and e[1] < height:
            # logger("e: x=%s, y=%s" % (e[0], e[1]))
            if grid[e[1]][e[0]] == "1":
                func(grid, e)
        pass

    return 0

