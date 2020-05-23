"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next
