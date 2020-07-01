"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \\     \
  5     4       <---
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        bfs = [root]
        res = []
        while bfs:
            bfs2 = []
            res.append(bfs[-1].val)
            for node in bfs:
                if node.left:
                    bfs2.append(node.left)
                if node.right:
                    bfs2.append(node.right)
            bfs = bfs2
        return res

