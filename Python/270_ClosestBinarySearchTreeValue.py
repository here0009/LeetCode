"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def dfs(node):
            if node:
                v = node.val - target
                if v > 0:
                    dfs(node.left)
                elif v < 0:
                    dfs(node.right)
                if abs(v) <= self.min_v:
                    self.min_v = abs(v)
                    self.res = node.val

        self.min_v = float('inf')
        self.res = None
        dfs(root)
        return self.res
