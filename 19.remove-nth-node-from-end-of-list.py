#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        probe = head
        if head.next is None:
            return None
        body = head 
        before = None
        for i in range(n - 1):
            probe = probe.next
        while probe.next:
            probe = probe.next
            before = body
            body = body.next 
        if before:
            before.next = body.next
            return head
        else:
            return body.next




# @lc code=end

