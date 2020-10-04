#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
class Solution:
    def findTimeForOne(self, i):
        if self.minTime[i] >= 0:
            return self.minTime[i] 
        if i == self.headID:
            self.minTime[i] = 0
            return 0
        self.minTime[i] = self.findTimeForOne(self.manager[i]) + self.informTime[self.manager[i]]
        return self.minTime[i]
        
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.n = n
        self.headID = headID
        self.manager = manager
        self.informTime = informTime
        minTime = [-1] * n
        self.minTime = minTime
        currentMax = -1
        for i in range(n):
            currentMax = max(currentMax, self.findTimeForOne(i))
        return currentMax

                
# @lc code=end

