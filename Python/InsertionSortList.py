"""
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def constructListNode(self, input_list):
        root = ListNode(0)
        curr = root
        for i in range(len(input_list)):
            curr.next = ListNode(input_list[i])
            curr = curr.next
        return root.next

    def insertionSortList(self, head: ListNode) -> ListNode:
        root = ListNode(0)
        root.next = head
        curr = head
        while curr and curr.next
            if curr.next.val < root.val:
                root.next = ListNode(curr.next.val)
                curr.next = curr.next.next
                root.next.next = curr

