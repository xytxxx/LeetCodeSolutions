#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        totalTime = 0
        L = len(timeSeries)
        if L == 0:
            return 0
        for i in range(L - 1):
            totalTime += min(timeSeries[i+1] - timeSeries[i], duration)
        return totalTime + duration 

# @lc code=end

