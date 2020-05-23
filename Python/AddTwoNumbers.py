# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = n = ListNode(0) #add a root, easy for the loop
        add_to_next = 0 #store the num add to next value
        while l1 or l2 or add_to_next:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            sum_val = v1 + v2 + add_to_next
            if  sum_val >= 10:
                add_to_next = 1
                val = sum_val - 10
            else :
                val = sum_val
                add_to_next = 0
            n.next = ListNode(val)
            n = n.next
        return root.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
l3 = s.addTwoNumbers(l1,l2)
print(l3.val, l3.next.val, l3.next.next.val)