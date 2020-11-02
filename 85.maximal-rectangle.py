#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        class Cell:
            def __init__(self, maxW, maxH):
                self.maxW = maxW
                self.maxH = maxH

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        # global maxSoFar
        maxSoFar = 0
        # def updateMax(x):
        #     global maxSoFar
        #     maxSoFar = max(maxSoFar, x)

        # [max height as going left], [max width as going up]
        sizeMap = [
            [
                Cell(0,0) for x in range(len(matrix[0]))
            ] for y in range(len(matrix))
        ]            
        if matrix[0][0] == '1':
            sizeMap[0][0] = Cell(1, 1)
            maxSoFar = 1
            
        for x in range(1, len(matrix[0])):
            if matrix[0][x] == '1':
                newMaxW = sizeMap[0][x-1].maxW + 1
                sizeMap[0][x].maxW = newMaxW
                sizeMap[0][x].maxH = 1
                if newMaxW > maxSoFar:
                    maxSoFar = newMaxW
        
        for y in range(1, len(matrix)):
            if matrix[y][0] == '1':
                newMaxH = sizeMap[y-1][0].maxH + 1
                sizeMap[y][0].maxH = newMaxH
                sizeMap[y][0].maxW = 1
                if newMaxH > maxSoFar:
                    maxSoFar = newMaxH

        for x in range(1, len(matrix[0])):
            for y in range(1, len(matrix)):
                if matrix[y][x] == '1':
                    newMaxH = sizeMap[y-1][x].maxH+1
                    sizeMap[y][x].maxH = newMaxH
                    newMaxW = sizeMap[y][x-1].maxW+1
                    sizeMap[y][x].maxW = newMaxW
                    maxSoFar = max(maxSoFar, newMaxH, newMaxW)
        
        # for row in sizeMap:
        #     str = ', '.join(map(lambda cell: '({},{})'.format(cell.maxW, cell.maxH), row))
        #     print(str)

        for x in range(1, len(matrix[0])):
            for y in range(1, len(matrix)):
                maxWForThisRow = sizeMap[y][x].maxW
                for up in range(1, sizeMap[y][x].maxH):
                    maxWForThisRow = min(sizeMap[y-up][x].maxW, maxWForThisRow)
                    maxSoFar = max(maxSoFar, ((up+1)*maxWForThisRow))

                maxHForThisRow = sizeMap[y][x].maxH
                for left in range(1, sizeMap[y][x].maxW):
                    maxHForThisRow = min(sizeMap[y][x-left].maxH, maxHForThisRow)
                    maxSoFar = max(maxSoFar, ((left+1)*maxHForThisRow))
        
        return maxSoFar

# @lc code=end

