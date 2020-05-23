"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        if head and head.next:
            even = head.next
        else:
            return head
        odd_root = odd
        even_root = even
        head = head.next.next
        counts = 2
        while head:
            counts += 1
            if counts % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
        even.next = None
        odd.next = even_root
        return odd_root

s = Solution()
l = [1,2,3,4,5]
def construtListNode(l):
    if not l:
        return None
    root = ListNode(l[0])
    node = root
    index = 1
    while index < len(l):
        node.next = ListNode(l[index])
        node = node.next
        index += 1
    return root
head = construtListNode(l)
# print(head.val)
# print(head.next.val)
# print(head.next.next.val)
head2 = s.oddEvenList(head)
while head2:
    print(head2.val)
    head2 = head2.next


l = [2,1,3,5,6,4,7]
head = construtListNode(l)
head2 = s.oddEvenList(head)
while head2:
    print(head2.val)
    head2 = head2.next

l = []
head = construtListNode(l)
head2 = s.oddEvenList(head)
while head2:
    print(head2.val)
    head2 = head2.next