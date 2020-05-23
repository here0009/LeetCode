# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        """
        if not root: #blank tree
            return root
        treeNodeTemp = TreeNode(0)
        if root.left or root.right: #left or right can be None
             self.invertTree(root.left)
             self.invertTree(root.right)
        treeNodeTemp = root.left
        root.left = root.right
        root.right = treeNodeTemp

        return root