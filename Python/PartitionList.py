"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Thoughts: 2 pointer, one for listnode, the other for the insert pos
    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_pre = ListNode(0)
        dummy_end = ListNode(0)
        # pre_insert = ListNode(0)
        # dummy_end = ListNode(0)
        pre_insert = dummy_pre
        end_insert = dummy_end
        node = head
        while node:
            if node.val < x:
                pre_insert.next = node
                pre_insert = pre_insert.next
            else:
                end_insert.next = node
                end_insert = end_insert.next
            node = node.next

        pre_insert.next = dummy_end.next
        end_insert.next = None
        return dummy_pre.next
            
