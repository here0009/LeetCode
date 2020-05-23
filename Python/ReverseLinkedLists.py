# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list_stack = []
        while head:
            list_stack.append(head.val)
            head = head.next

            
        len_list = len(list_stack)
        for i in range(1, len_list):
            listnode = ListNode(list_stack[i]) 
            listnode.next = list_stack[i-1]

        return listnode



            