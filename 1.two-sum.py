#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
        for i, a in enumerate(nums):
            b = target - a
            if b in dic:
                if a == b and len(dic[a]) >= 2:
                    return tuple(dic[a])
                elif a != b:
                    return (dic[a][0], dic[b][0])
        return (0, 0)
# @lc code=end

