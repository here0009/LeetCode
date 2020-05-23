"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \\    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def dfs(self, root: TreeNode, total: int, path = []):
        if not root:
            return
        total = total - root.val
        path = path + [root.val]
        if total == 0 and not root.left and not root.right:
            self.res.append(path)
            return
        self.dfs(root.left, total, path)
        self.dfs(root.right, total, path)

    def pathSum(self, root: TreeNode, total: int):
        self.dfs(root, total)
        return self.res

node_vals = [5,4,8,11,13]