"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 """
 # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def sortedArrayToBST(self, nums) -> TreeNode:
        len_n = len(nums)
        if len_n == 0:
            return None
        elif len_n == 1:
            return TreeNode(nums[0])
        else:
            mid = len_n//2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root

class Solution:
    """
    passing index, rather than the list
    """
    def sortedArrayToBST(self, nums) -> TreeNode:
        def helper(lower, upper):
            if lower == upper:
                return None
            mid = (lower + upper) //2
            node = TreeNode(nums[mid])
            node.left = helper(lower, mid)
            node.right = helper(mid+1, upper)
            return node

        return helper(0, len(nums))

s = Solution()
nums = [-10,-3,0,5,9]
root = s.sortedArrayToBST(nums)
print(root.val)
print(root.left.val)
print(root.left.left.val)