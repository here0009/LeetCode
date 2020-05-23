"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.

def constructListNode(input_list):
    root = ListNode(0)
    curr = root
    for i in range(len(input_list)):
        curr.next = ListNode(input_list[i])
        curr = curr.next
    return root.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import deque
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root = ListNode(0)
        
        root.next = head
        pre = root
        curr = root.next
        dq = deque()
        
        while curr:
            index = 0
            while index < k and curr:
                dq.append(curr)
                curr = curr.next
                index += 1
            while dq:
                if index < k:
                    pre.next = dq.popleft()
                    pre = pre.next
                else:
                    pre.next = dq.pop()
                    pre = pre.next
        pre.next = None
        return root.next

input_list = [1,2,3,4,5]
head = constructListNode(input_list)
s = Solution()
new_head = s.reverseKGroup(head, 3)
# print(new_head.val, new_head.next.val)
while new_head:
    print(new_head.val)
    new_head = new_head.next

print("=====")
head = constructListNode(input_list)
new_head = s.reverseKGroup(head, 2)
while new_head:
    print(new_head.val)
    new_head = new_head.next
