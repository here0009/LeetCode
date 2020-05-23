# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if (p and q) and (p.val != q.val):
            return False
        if (p.left and not q.left) or (not p.left and q.left):
            return False
        if (p.right and not q.right) or (not p.right and q.right):
            return False 
        if (p.left and q.left) and (not self.isSameTree(p.left, q.left)):
            return False
        if (p.right and q.right) and (not self.isSameTree(p.right, q.right)):
            return False
        return True