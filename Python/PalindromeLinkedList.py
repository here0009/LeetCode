# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        for i in range(len(stack)//2):
            if stack[i] != stack[-1 * (i+1)]:
                return False
        return True
