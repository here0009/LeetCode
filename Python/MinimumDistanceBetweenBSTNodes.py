"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \\    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.res = float('inf')
        def dfs(root):
            if not root:
                return
            if root.left:
                left = root.left
                while left.right:
                    left = left.right
                self.res = min(root.val - left.val, self.res)
                dfs(root.left)
            if root.right:
                right = root.right
                while right.left:
                    right = right.left
                self.res = min(right.val - root.val, self.res)
                dfs(root.right)
        dfs(root)
        return self.res

