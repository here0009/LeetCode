"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        d_head = dummy
        pre = head
        curr = head.next
        while curr:
            if pre.val != curr.val:
                d_head.next = pre
                d_head = d_head.next
            else:
                while curr and curr.val == pre.val:
                    curr = curr.next
            if curr:
                pre, curr = curr, curr.next
                if curr is None: #the last node is unique
                    d_head.next = pre
                    d_head = d_head.next

        d_head.next = None
        # node = dummy.next
        # while node:
        #     print(node.val)
        #     node = node.next
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head #head linked to pre temporarily, if head.val == head.next.val, head.next.next will link to pre
            else:
                pre = pre.next
                head = head.next
            
        # node = dummy.next
        # while node:
        #     print(node.val)
        #     node = node.next
        return dummy.next


l = [1,2,3,3,4,4,5]
# l = [1,1,1,2,3]
head = ListNode(l[0])
node = head
for i in range(1,len(l)):
    node.next = ListNode(l[i])
    node = node.next

s = Solution()
print(s.deleteDuplicates(head))