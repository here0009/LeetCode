"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        counts = 0
        stack = []
        dummy = ListNode(0)
        pre = dummy
        while head:
            counts += 1
            if counts < m:
                pre.next = head
                pre = pre.next
            elif counts >=m and counts <=n:
                stack.append(head)
            else:
                break
            head = head.next

        while stack:
            pre.next = stack.pop()
            pre = pre.next
        pre.next = head

        return dummy.next
                    
            
