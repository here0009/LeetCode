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

def constructLinkedList(nodes):
    head = ListNode(nodes[0])
    original_head = head
    for val in nodes[1:]:
        head.next = ListNode(val)
        head = head.next
    return original_head



class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        while head and head.next and head.val == head.next.val: 
            if head.next.next:
                if head.next.val == head.next.next.val:
                    head.next = head.next.next
                else:
                    head = head.next.next
            else:
                head = None

        original_head = head
        while head and head.next:
            # print(head.val,head.next.val)
            if head.val == head.next.val:
                if head.next.next:
                    if head.next.val == head.next.next.val:
                        head.next = head.next.next
                    else:
                        head = head.next.next
                        # print(head.val)
                        # if head.next.next:                            
                else:
                    head = None
            else:
                head = head.next
        return original_head




s = Solution()
nodes = [1,2,3,3,4,4,5]
head = constructLinkedList(nodes)
print(head.val,head.next.val,head.next.next.val,head.next.next.next.val,head.next.next.next.next.val)
head = s.deleteDuplicates(head)
print(head.val,head.next.val,head.next.next.val,head.next.next.next.val,head.next.next.next.next.val)

# nodes = [1,1,1,2,3]
# head = constructLinkedList(nodes)
# print(head.val,head.next.val,head.next.next.val)
# s = Solution()
# head = s.deleteDuplicates(head)
# print(head.val,head.next.val)