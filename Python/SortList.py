"""
Sort a linked list in O(n log n) time using constant space complexity.

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
    def constructListNode(self, input_list):
        root = ListNode(0)
        curr = root
        for i in range(len(input_list)):
            curr.next = ListNode(input_list[i])
            curr = curr.next
        return root.next
        
    def sortList(self, head: ListNode) -> ListNode:
        ln_list = []
        while head:
            ln_list.append(head.val)
            head = head.next

        ln_list = sorted(ln_list)
        res = self.constructListNode(ln_list)
        # print(res.val, res.next.val)
        return res

class Solution:
    """
    merge sort
    """
    def constructListNode(self, input_list):
        root = ListNode(0)
        curr = root
        for i in range(len(input_list)):
            curr.next = ListNode(input_list[i])
            curr = curr.next
        return root.next

    def merge(self, head1, head2):
        root = ListNode(0)
        curr = root
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        curr.next = head1 or head2
        return root.next
        
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast,slow = head,head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        res = self.merge(self.sortList(head), self.sortList(second))
        # print(res.val, res.next.val)
        return res 


s = Solution()
input_list = [4,2,1,3]
ln = s.constructListNode(input_list)
res = s.sortList(ln)
print(res.val, res.next.val)

input_list = [-1,5,3,4,0]
ln = s.constructListNode(input_list)
res = s.sortList(ln)
print(res.val, res.next.val)
