"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        original_head = head
        while head.next:
            if head.val == head.next.val:
                if head.next.next:
                    head.next = head.next.next
                else:
                    head.next = None
            else:
                head = head.next
        return original_head


def constructLinkedList(nodes):
    head = ListNode(nodes[0])
    original_head = head
    for val in nodes[1:]:
        head.next = ListNode(val)
        head = head.next
    return original_head

nodes = [1,1,2]
head = constructLinkedList(nodes)
print(head.next.val)
s = Solution()
print(s.deleteDuplicates(head).next.val)

nodes = [1,1,2,3,3]
head = constructLinkedList(nodes)
print(head.next.next.val)
s = Solution()
print(s.deleteDuplicates(head).next.next.val)