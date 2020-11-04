"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        l, r = 0, len(lst)-1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True
