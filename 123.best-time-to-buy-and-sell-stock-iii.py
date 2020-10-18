#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#


# 3,3,4,0,0,3,1,4

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def findNewStratForward(endIndex: int, bestProfit: int, minIndexBefore: int):
            if prices[endIndex] - prices[minIndexBefore] > bestProfit:
                return (minIndexBefore, endIndex), -1
            elif prices[endIndex] < prices[minIndexBefore]:
                return (-1, -1), endIndex
            else:
                return (-1, -1), -1

        def findNewStratBackward(beginIndex, bestProfit, maxIndexBefore):
            if prices[maxIndexBefore] - prices[beginIndex] > bestProfit:
                return (beginIndex, maxIndexBefore), -1
            elif prices[beginIndex] > prices[maxIndexBefore]:
                return (-1, -1), beginIndex
            else:
                return (-1, -1), -1

        bestProfit = 0
        bestStrat = (-1, -1)
        minIndex = 0
        bestProfitForward = [0] * len(prices)
        for endIndex in range(1, len(prices)):
            newStrat, newMinIndex = findNewStratForward(endIndex, bestProfit, minIndex)
            if newStrat[0] >= 0:
                bestStrat = newStrat
                bestProfit = prices[bestStrat[1]] - prices[bestStrat[0]]
            bestProfitForward[endIndex] = bestProfit

            minIndex = newMinIndex if newMinIndex >= 0 else minIndex
        singleTransBestProfit = bestProfit


        bestProfit = 0
        bestStrat = (-1, -1)
        maxIndex = len(prices) - 1
        bestProfitBackward = [0] * len(prices)
        for beginIndex in range(len(prices) - 2, 0, -1):
            newStrat, newMaxIndex = findNewStratBackward(beginIndex, bestProfit, maxIndex)
            if newStrat[0] >= 0:
                bestStrat = newStrat
                bestProfit = prices[bestStrat[1]] - prices[bestStrat[0]]
            bestProfitBackward[beginIndex] = bestProfit

            maxIndex = newMaxIndex if newMaxIndex >= 0 else maxIndex
        
        bestProfit = 0
        for divide in range(len(prices) - 1):
            profit = bestProfitForward[divide] + bestProfitBackward[divide+1] 
            bestProfit = profit if profit > bestProfit else bestProfit

        return max(bestProfit, singleTransBestProfit)


# @lc code=end

