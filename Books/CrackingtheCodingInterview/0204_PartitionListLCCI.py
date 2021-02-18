"""
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

Example:

Input: head = 3->5->8->5->10->2->1, x = 5
Output: 3->1->2->10->5->5->8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        s1, s2 = [], []
        while head:
            if head.val < x:
                s1.append(head)
            else:
                s2.append(head)
            head = head.next
        s = s1 + s2
        head = s[0]
        node = head
        s[-1].next = None
        for nxt_node in s[1:]:
            node.next = nxt_node
            node = node.next
        return head


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre, curr = head, head
        while curr:  # pre is where the listnode split
            if curr.val < x:
                pre.val, curr.val = curr.val, pre.val
                pre = pre.next
            curr = curr.next
        return head


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1 = p = ListNode(-1)
        l2 = q = ListNode(-1)
        while head:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next
        p.next, q.next = l2.next, None
        return l1.next

