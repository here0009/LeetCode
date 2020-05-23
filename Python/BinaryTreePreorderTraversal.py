"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        def pTraveresal(root):
            if root:
                res.append(root.val)
                pTraveresal(root.left)
                pTraveresal(root.right)

        res = []
        pTraveresal(root)
        return res

