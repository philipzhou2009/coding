# https://leetcode.com/problems/path-with-maximum-gold/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        
        pass


def getResult(grid, point, past):
    
    x = point[0]
    y = point[1]
    
    currentGold = grid[y][x]
    print("currentGold=", currentGold)
    
    if currentGold == 0:
        return 0
    
    cols = len(grid[0])
    rows = len(grid)
    
    nextPoints = []
    
    # top
    if y > 0:
        pointTop = [x, y-1]
        if not pointTop in past:
            nextPoints.append(pointTop)
    
    if y < rows-1:
        pointBottom = [x, y+1]
        if not pointBottom in past:
            nextPoints.append(pointBottom)
        
    if x > 0:
        pointLeft = [x-1, y]
        if not pointLeft in past:
            nextPoints.append(pointLeft)
        
    if x < cols-1:
        pointRight = [x+1, y]
        if not pointRight in past:
            nextPoints.append(pointRight)
        
    print("nextPoints=", nextPoints)
    
    nPoints = len(nextPoints)
    if nPoints == 0:
        return 0
    
    
    past.append(point)
    max = None
    for p in nextPoints:
        pathLen = getResult(grid, p, past)
        max = pathLen if max == None or pathLen > max else max
        
    
    result = currentGold + max 
     
    return result
    



# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# result = getResult([[0,6,0],[5,8,7],[0,9,0]], [1, 2], [])   


# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
result = getResult(grid, [0,0], [])
print("result=", result)