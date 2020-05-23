"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 """
 # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def helper(lower, upper):
            if lower == upper:
                return None
            mid = (lower + upper) //2
            node = TreeNode(nums[mid])
            node.left = helper(lower, mid)
            node.right = helper(mid+1, upper)
            return node

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return helper(0, len(nums))



class Solution:
    def findMid(self,head):
        prePointer = None
        slowPointer = head
        fastPointer = head
        while fastPointer and fastPointer.next:
            prePointer = slowPointer
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        if prePointer:
            prePointer.next = None
        return slowPointer

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        mid = self.findMid(head)
        node = TreeNode(mid.val)
        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
