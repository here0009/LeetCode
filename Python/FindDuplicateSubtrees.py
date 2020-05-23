"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root):
        def dfs(root):
            if not root:
                return ''
            left = dfs(root.left)
            right = dfs(root.right)
            string = '(' + left + str(root.val) + right + ')' #a unique indentifier of the node
            node_dict[string].append(root)
            return string


        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        node_dict = defaultdict(list)
        dfs(root)
        res = []
        for key,vals in node_dict.items():
            if len(vals) > 1:
                res.append(vals[0])
        return res


