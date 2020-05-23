"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, sign):
            if node:
                if sign == 0:
                    if node.left:
                        self.res += node.left.val
                    if node.right:
                        self.res += node.right.val
                dfs(node.left, node.val % 2)
                dfs(node.right, node.val % 2)

        self.res = 0
        dfs(root.left, root.val%2)
        dfs(root.right, root.val%2)
        return self.res


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandparent):
            if node:
                if grandparent and grandparent.val % 2 == 0:
                    self.res += node.val
                dfs(node.left, node, parent)
                dfs(node.right, node, parent)

        self.res = 0
        dfs(root, None, None)
        return self.res