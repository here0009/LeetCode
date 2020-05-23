"""
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        res = []
        if N%2:
            return res
        root = TreeNode(0)
        if N == 1:
            res.append(None)
            res.append(None)
            return
        if N == 3:
            root.left = TreeNode(0)
            root.right = TreeNode(0)
        else:
            root.left = allPossibleFBT(N-2)
            roo.right = allPossibleFBT(N-2)
        
        res.append(root)

        return res
        