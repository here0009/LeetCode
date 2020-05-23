"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_1:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        Thoughts: use a stack
        """
        stack = []
        counts = 0
        node = head
        while node:
            counts += 1
            stack.append(node)
            node = node.next

        node = head
        index = 0
        while index < counts:
            if index % 2 == 0:
                tmp = node.next
                node.next = stack.pop()
            else:
                node.next = tmp
            node = node.next
            index += 1

        if node:
            node.next = None

        # node = head
        # while node:
        #     print(node.val)
        #     node = node.next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        Thoughts: reverse tha last half of the ListNode
        """
        if not head:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the ListNode inplace
        pre, curr = None, slow
        while curr: 
            pre, curr.next, curr = curr, pre, curr.next

        # while node:
        #     pre, node.next, node = node, pre, node.next

        first, second = head, pre
        while second.next:
        # while first and second : #not right, will lead to an infinite cycle
            first.next, first = second, first.next
            second.next, second = first, second.next
        

        node = head
        while node:
            print(node.val)
            node = node.next

class Solution_2:
    def reorderList(self, head):
        if not head:
            return
            
        # find the mid point
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next
        
        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        node = head
        while node:
            print(node.val)
            node = node.next
        return

from LeetCode import constructListNode
s = Solution()
l = [1,2,3,4]
head = constructListNode(l)
s.reorderList(head)
l = [1,2,3,4,5]
head = constructListNode(l)
s.reorderList(head)