"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \\   \
          1   1   5
Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \\   \
          4   4   5
Output: 2

 

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, value):
            if node:
                if node.val == value:
                    left = dfs(node.left, value)
                    right = dfs(node.right, value)
                    self.res = max(left+right, self.res)
                    return max(left, right) +1
                else:
                    dfs(node, node.val)
                    return 0
            else:
                return 0

        if not root:
            return self.res
        dfs(root, root.val)
        return self.res
        