#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def numToSkip (rowNum):
            down = (numRows - rowNum -1) * 2 - 1
            up = (rowNum) * 2 - 1
            return up + 1, down + 1
        

        if numRows == 1:
            return s
        
        result = ''

        for firstLetterIndex in range(numRows):
            upSkip, downSkip = numToSkip(firstLetterIndex)
            goingDown = True
            doNotAppend = False
            cursor = firstLetterIndex
            while cursor < len(s):
                if not doNotAppend:
                    result += s[cursor]
                doNotAppend = False
                if goingDown:
                    goingDown = False
                    if downSkip <= 0:
                        doNotAppend = True
                        continue
                    cursor += downSkip
                else:
                    goingDown = True
                    if upSkip <= 0:
                        doNotAppend = True
                        continue
                    cursor += upSkip
        return result

# @lc code=end

