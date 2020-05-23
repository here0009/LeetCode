"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1
Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
"""

"""
minnimum aboslute difference of a node is either min(node.righttree) - node.val or node.val - max(node.lefttree)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left or root.right:


    def minDiffNode(self, node):
        """
        :type root: TreeNode
        :rtype: int
        """
        tmp_left = node
        tmp_right = node
        if node.right:
            tmp_right = node.right
            while  

        