#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.next is None and l1.val == 0:
            return l2
        if l2.next is None and l2.val == 0:
            return l1
        increment = 0
        l1Cursor = l1
        l2Cursor = l2
        result = ListNode(0, None)
        first = True
        prevResultNode = result
        while l1Cursor and l2Cursor:
            sum = l1Cursor.val + l2Cursor.val + increment
            increment, sum = (1, sum - 10) if sum >= 10 else (0, sum)
            l1Cursor = l1Cursor.next
            l2Cursor = l2Cursor.next    
            newNode = ListNode(sum, None)
            if first:
                prevResultNode.val = sum
                first = False
            else:
                prevResultNode.next = newNode
                prevResultNode = newNode
        restCursor = l1Cursor if l1Cursor else l2Cursor
        while restCursor and restCursor.val + increment >= 10:
            sum = restCursor.val + increment
            increment, sum = (1, sum - 10) if sum >= 10 else (0, sum)
            restCursor = restCursor.next
            newNode = ListNode(sum, None)
            prevResultNode.next = newNode
            prevResultNode = newNode
        if restCursor:
            newNode = ListNode(restCursor.val + increment, restCursor.next)
            prevResultNode.next = newNode
        elif increment > 0:
            prevResultNode.next = ListNode(increment, None) 
        return result

# @lc code=end

