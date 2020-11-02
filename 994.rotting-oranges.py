#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from typing import Tuple


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        H = len(grid)
        W = len(grid[0])
        def adjacent(x, y):
            res = [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]
            if x == 0 or grid[x-1][y] == 2:
                res.remove((x-1, y))
            if x == H - 1 or grid[x+1][y] == 2:
                res.remove((x+1, y))
            if y == W - 1 or grid[x][y+1] == 2:
                res.remove((x, y + 1))
            if y == 0 or grid[x][y-1] == 2:
                res.remove((x, y - 1))
            return res


        frontier = set([])
        numFresh = 0
        for x in range(H):
            for y in range(W):
                if grid[x][y] == 2:
                    adj = adjacent(x, y)
                    for p in adj:
                        frontier.add(p)
                elif grid[x][y] == 1:
                    numFresh += 1

        time = 0 
        while numFresh > 0:
            newFront = set([])
            if len(frontier) == 0:
                return -1
            for x, y in frontier:
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    numFresh -= 1
                    adj = adjacent(x, y)
                    for p in adj:
                        newFront.add(p)
            time += 1
        return time






# @lc code=end

