"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \\  \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \\  \
2   4   7

Target = 28

Output: False
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        s = set()
        def dfs(root,k):
            if not root:
                return False
            s.add(root.val)
            if k - root.val in s:
                return True
            return dfs(root.left,k) or dfs(root.right,k)

        return dfs(root,k)



        