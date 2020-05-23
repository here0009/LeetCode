# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode):
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                self.res.append(node.val)
        self.res = []
        dfs(root)
        return self.res
            
from collections import deque
class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        if not root:
            return res
        bfs = deque([root])
        while bfs:
            node = bfs.popleft()
            if node.left:
                bfs.appendleft(node.left)
            if node.right:
                bfs.appendleft(node.right)
            res.append(node.val)
        return reversed(res)



class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        if not root:
            return res
        bfs = [root]
        while bfs:
            node = bfs.pop()
            res.append(node.val)
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        return reversed(res)