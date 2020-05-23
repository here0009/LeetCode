"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow-up:
Can you solve it without using extra space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        wrong
        """
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        # counts = 0
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # counts += 1
            if slow is fast:
                return slow.next    
        return None

"""
https://leetcode.com/problems/linked-list-cycle-ii/discuss/258948/%2B-python
the distance before cylce is H, from cycle start to meeting point is D, the distance of the cycle is C.
so, 2(H+D) = H+D+nC
H + D = nC
"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        try:
            slow = slow.next
            fast = head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        slow = head #set slow back to head, slow will travel h, fast will travel nC-D, they will meet at the start point of the cycle
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow