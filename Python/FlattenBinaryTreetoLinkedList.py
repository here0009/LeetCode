"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \\   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        node = root
        while node:
            # print(node.val)
            if node.left:
                if node.right:
                    stack.append(node.right)
                node.right = node.left
                node.left = None
            elif node.right:
                node = node.right
                continue
            elif len(stack) > 0:
                node.right = stack.pop()
            node = node.right
