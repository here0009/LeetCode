"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from LeetCode import Tree_Builds_BFS

# from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        q = [root]
        res = []
        if not root:
            return res
        while q:
            new_q = []
            tmp = []
            for node in q:
                tmp.append(node.val)
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            res.append(tmp)
            q = new_q
        return res[::-1]

vals = [3,9,20,None,None,15,7]
root = Tree_Builds_BFS(vals)
print(root.val)
print(root.right.val)
s = Solution()
print(s.levelOrderBottom(root))
print(s.levelOrderBottom(None))         
