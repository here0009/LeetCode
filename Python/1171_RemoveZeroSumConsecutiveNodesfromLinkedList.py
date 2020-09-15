"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""


# Definition for singly-linked list.
from LeetCode import constructListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import OrderedDict
class Solution_1:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        ln = []
        while head:
            ln.append(head.val)
            head = head.next
        preSum = OrderedDict()
        preSum[0] = -1
        tmp = 0
        for i,v in enumerate(ln):
            tmp += v
            # print(preSum)
            j = preSum.get(tmp, i)
            while tmp in preSum:
                preSum.popitem()
            preSum[tmp] = j
        lst = [ln[i] for v,i in preSum.items()]
        curr = dummy = ListNode(lst[0])
        for v in lst[1:]:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

#https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366319/JavaC%2B%2BPython-Greedily-Skip-with-HashMap
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/414285/Python-easy-to-understand-solution-with-explanations
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        prefix = 0
        seen = {}
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next
        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        return dummy.next

from collections import OrderedDict
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        dummy.next = head
        prefix = 0
        seen = OrderedDict()
        while curr:
            prefix += curr.val
            node = seen.get(prefix, curr)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            curr = curr.next
            node.next = curr
        return dummy.next

S = Solution_1()
head = constructListNode([1,2,-3,3,1])
print(S.removeZeroSumSublists(head))
head = constructListNode([1,2,3,-3,4])
print(S.removeZeroSumSublists(head))
head = constructListNode([1,2,3,-3,-2])
print(S.removeZeroSumSublists(head))