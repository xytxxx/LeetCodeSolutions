#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        state = {
            '(' : False,
            '[' : False,
            '{' : False
        }
        corre = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        corre2 = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        lastOpen = []
        openBrs = set(['(', '[', '{'])
        for char in s:
            if char in openBrs:
                if state[char]:
                    return False
                state[char] = True
                lastOpen.append(char)
            else:
                if not state[corre2[char]] or corre[lastOpen.pop()] != char:
                    return False
                state[corre2[char]] = False
        return not any(state.values())
# @lc code=end

