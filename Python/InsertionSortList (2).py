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

class Solution_1:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        node = dummy
        # head = head.next #start from the 2nd
        while head:
            # print(head.val)
            insert_node = dummy
            tmp = head.next
            while insert_node.next and head.val > insert_node.next.val:
                insert_node = insert_node.next  
                # tmp = insert_node.next
            if not insert_node.next:
                insert_node.next = head
                head.next = None
            else:
                head.next = insert_node.next
                insert_node.next = head
            head = tmp
 
        # node = dummy.next
        # while node:
        #     print(node.val)
        #     node = node.next

        return dummy.next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        while head and head.next:
            # print(head.val)
            if head.val < head.next.val:
                head = head.next
                continue
            pre = dummy
            val = head.next.val
            tmp = head.next #node to insert
            while pre.next and pre.next.val < val:
                pre = pre.next
            # pre.next, head.next.next, head.next = head.next, pre.next, head.next.next
            tmp = head.next
            head.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp

        # node = dummy.next
        # while node:
        #     print(node.val)
        #     node = node.next

        return dummy.next

# l = [-1,5,3,4,0]
l = [4,2,1,3]
head = ListNode(l[0])
node = head
for i in range(1,len(l)):
    node.next = ListNode(l[i])
    node = node.next

s = Solution()
print(s.insertionSortList(head))