"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def dfs(node):
            if not node:
                return 1
            v = node.val + dfs(node.next)
            node.val = v % 10
            return v //10

        v = dfs(head)
        if v > 0:
            root = ListNode(1)
            root.next = head
        else:
            root = head
        return root