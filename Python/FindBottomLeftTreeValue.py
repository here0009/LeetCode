"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def depth(root):
            if not root.left and root.right:
                return 1
            if root.left:
                return 1+depth(root.left)
            if root.right:
                return 1+depth(root.right, n+1)

            
        if depth(root.left) < depth(root.right):
            return root.right.val
        return root.left.val

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
        BFS
        """
        q = [root]
        while q:
            q2 = []
            for node in q:
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            # print([node.val for node in q2])
            if len(q2) == 0:
                return q[0].val
            else:
                q = q2
        return None

s = Solution
