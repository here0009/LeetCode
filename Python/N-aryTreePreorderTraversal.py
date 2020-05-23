"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

Note:

Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution_1:
    def preorder(self, root: 'Node') -> 'List[int]':
        res = []
        def dfs(root):
            if root:
                res.append(root.val)
                for node in root.children:
                    dfs(node)
        dfs(root)
        return res

#Iterative solution
class Solution:
    def preorder(self, root: 'Node') -> 'List[int]':
        if not root:
            return []
        q = [root]
        res = []
        while q:
            node = q.pop()
            res.append(node.val)
            q.extend(reversed(node.children))
        return res

