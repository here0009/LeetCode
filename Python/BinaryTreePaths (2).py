"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        res = []
        def dfs(root, path):
            if not root:
                return
            path = path + [str(root.val)]
            if not root.left and not root.right:
                res.append('->'.join([s for s in path]))
            else:
                if root.left:
                    dfs(root.left, path)
                if root.right:
                    dfs(root.right, path)

        dfs(root,[])
        return res

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        res = []
        def dfs(root, path):
            if not root:
                return
            path = path + [root.val]
            if not root.left and not root.right:
                res.append('->'.join(str(i) for i in path))
            dfs(root.left, path)
            dfs(root.right, path)

        dfs(root,[])
        return res