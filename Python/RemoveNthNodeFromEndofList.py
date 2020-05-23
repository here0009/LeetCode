"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nhead = head
        dummy = ListNode(0)
        dummy.next = head
        if not head or n == 0:
            return head
        counts = 0
        while counts < n:
            nhead = nhead.next
            counts += 1
            # if not nhead:
            #     print('test')
                # return None

        if not nhead: #remove head
            dummy.next = dummy.next.next
            return dummy.next
        node = head
        while nhead.next:
            node = node.next
            nhead = nhead.next

        if node.next:
            node.next = node.next.next
        else:
            return None

        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        node, nhead = dummy, dummy #set node and nhead to dummy
        counts = 0
        while counts < n+1: #use n+1 instead of n
            nhead = nhead.next
            counts += 1

        while nhead:
            nhead = nhead.next
            node = node.next

        node.next = node.next.next
        return dummy.next

from LeetCode import constructListNode
from LeetCode import printListNode
s = Solution()
# l = [1,2,3,4]
# head = constructListNode(l)
# # for i in range(4):
# printListNode(s.removeNthFromEnd(head,i))


l = [1,2,3,4,5]
head = constructListNode(l)
# for i in range(5):
printListNode(s.removeNthFromEnd(head,5))

l = [1,2]
head = constructListNode(l)
printListNode(s.removeNthFromEnd(head,2))

"""
Output
[]
Expected
[2]
"""