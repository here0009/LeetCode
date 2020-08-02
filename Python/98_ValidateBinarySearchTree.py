"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        wrong answer
        """
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        if not self.isValidBST(root.left) or not self.isValidBST(root.right):
            return False
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node):
            if node:
                dfs(node.left)
                node_list.append(node.val)
                dfs(node.right)

        node_list = []
        dfs(root)
        for i in range(1, len(node_list)):
            if node_list[i] <= node_list[i-1]:
                return False
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not dfs(node.left, lower, val):
                return False
            if not dfs(node.right, val, upper):
                return False
            return True

        return dfs(root, float('-inf'), float('inf'))