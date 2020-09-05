#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLengthSoFar = 0
        prevLength = 0
        letterToLastIndex = {}
        for i, letter in enumerate(s):
            if letter not in letterToLastIndex or letterToLastIndex[letter] < i - prevLength:
                thisLength = prevLength + 1
            else:
                lastAppearance = letterToLastIndex[letter]
                thisLength = min(i - lastAppearance, prevLength + 1)
            letterToLastIndex[letter] = i
            maxLengthSoFar = max(maxLengthSoFar, thisLength)
            prevLength = thisLength
        return maxLengthSoFar
            
# @lc code=end