"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            l_depth, l_balance = dfs(root.left)
            r_depth, r_balance = dfs(root.right)
            depth = 1 + max(l_depth, r_depth)
            if not l_balance or not r_balance:
                return depth, False
            if abs(l_depth - r_depth) > 1:
                return depth,False
            return depth,True

        d, tf = dfs(root)
        return tf

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if l == -1 or r == -1:
                return -1
            if abs(l-r) > 1:
                return -1
            return 1 + max(l, r)

        return not dfs(root) == -1



class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return not self.helper(root) == -1
    
    
    
    def helper(self,root):
        if not root: return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        if l == -1 or r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return max(l,r) + 1