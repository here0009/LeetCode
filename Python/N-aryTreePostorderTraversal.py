"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].

 
Note:

Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution_1:
    def postorder(self, root: 'Node') -> 'List[int]':
        res = []
        def dfs(root):
            if root.children:
                for node in root.children:
                    dfs(node)
            res.append(root.val)
        
        if not root:
            return res
        dfs(root)
        return res

class Solution:
    def postorder(self, root: 'Node') -> 'List[int]':
        if not root:
            return []
        q = [root]
        res = []
        while q:
            node = q.pop()
            if node.children:
                q.extend(reversed(node.children))
            res = node.val
        return res