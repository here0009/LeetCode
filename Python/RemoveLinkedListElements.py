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
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        tmp = head
        while tmp.val == val:
            #remove the head if it eaquals to val
            tmp = tmp.next

        while tmp:
            if tmp.next: 
                if tmp.next.val == val:
                    tmp.next = tmp.next.next
            else:
                tmp.next = None
            tmp = tmp.next
        return head

s = Solution()
l = [2,6,3,4,5,6,1]
head = ListNode(1)
tmp = head
for num in l:
    node = ListNode(num)
    tmp.next = node
    print(tmp.next.val)
    tmp = tmp.next

print("##########")
s.removeElements(head, 1)

tmp = head
while tmp:
    print(tmp.val)
    tmp = tmp.next