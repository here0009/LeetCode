
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        stack = []
        while head:
            stack.append(head)
            head = head.next
        root = node = stack.pop()
        while stack:
            node.next = stack.pop()
            node = node.next
        node.next = None
        return root
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preNode = None
        while head:
            tmpNode = head.next
            head.next = preNode
            preNode = head
            head = tmpNode
        return preNode