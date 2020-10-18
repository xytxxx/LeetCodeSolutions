#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        L = len(words)
        arr = [[False for i in range(26)] for j in range(L)]
        for i, word in enumerate(words):
            for letter in word:
                char = ord(letter) - ord('a')
                arr[i][char] = True


        for i, word in enumerate(words):
            for j in range(i+1, L):
                for char in 
                    char = ord(letter) - ord('a')

# @lc code=end

