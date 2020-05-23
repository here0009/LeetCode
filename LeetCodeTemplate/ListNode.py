"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def constructListNode(self, input_list):
    #     root = ListNode(input_list[0])
    #     res = root
    #     for i in range(1,len(input_list)):
    #         root.next = ListNode(input_list[i])
    #         root = root.next
    #     return res
    def constructListNode(self, input_list):
        root = ListNode(0)
        curr = root
        for i in range(len(input_list)):
            curr.next = ListNode(input_list[i])
            curr = curr.next
        return root.next
        
    def LNtoint(self, input_ln):
        res = 0
        while input_ln:
            res = res*10 + l1.val
            l1 = l1.next
        return res

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        res_int = self.LNtoint(l1) + self.LNtoint(l2)
        if res_int == 0:
            return ListNode(0)
        res_list = []
        while res_int > 0:
            res_int, rmd = divmod(res_int, 10)
            res_list.append(rmd)
        res_list = res_list[::-1]
        res = self.constructListNode(res_list)

        return res

def constructListNode(input_list):
    root = ListNode(0)
    curr = root
    for i in range(len(input_list)):
        curr.next = ListNode(input_list[i])
        curr = curr.next
    return root.next

s = Solution()
l1 = s.constructListNode([7,2,4,3])
l2 = s.constructListNode([5,6,4])
print(l1.val, l1.next.val, l1.next.next.val, l1.next.next.next.val)
print(l2.val, l2.next.val, l2.next.next.val)
print(s.addTwoNumbers(l1,l2))

l1 = s.constructListNode([0])
l2 = s.constructListNode([0])
print(l1.val)
print(l2.val)
print(s.addTwoNumbers(l1,l2))