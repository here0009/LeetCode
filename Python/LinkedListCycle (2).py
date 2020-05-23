"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    wrong
    """
    def hasCycle(self, head: ListNode) -> bool:
        num = 0^head.val
        head = head.next
        while head:
            num2 = head.val ^ num
            if num2 == head.val:
                return True
            head = head.next
            num = num2
        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node_set = set()
        while head:
            if head in node_set:
                return True
            else:
                node_set.add(head)
                head = head.next
        return False


class Solution:
    """
    a faster runner and a slower runner will meet if there is a cycle
    """
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow and fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False
            