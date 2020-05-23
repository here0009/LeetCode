"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
from LeetCode import constructListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = ListNode(0)
        root.next = head
        pre,curr = root,root.next
        while curr and curr.next:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = curr
            pre.next = tmp
            pre, curr = curr, curr.next
        return root.next


# class Solution: 
    # wrong answer, should replace curr.next with a name
#     def swapPairs(self, head: ListNode) -> ListNode:
#         root = ListNode(0)
#         root.next = head
#         pre,curr = root,root.next
#         while curr and curr.next:
#             # tmp = curr.next
#             curr.next = curr.next.next
#             curr.next.next = curr
#             pre.next = curr.next
#             pre, curr = curr, curr.next
#         return root.next



ln = constructListNode([1,2,3,4])
print(ln.val)
s = Solution()
head = s.swapPairs(ln)
while head:
    print(head.val)
    head = head.next