"""
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.

        return the max node from left subtree and min node from right subtree
        if there is a mistake, swap the two nodes, find their parent first
        swap the max node in left subtree and min node in right subtree
        """
        # wrong answer
        def dfs(node):
            if not node:
                return None
            left, right = node, node
            if node.left:
                left_node = dfs(node.left)
                if left_node.val > node.val:
                    left = left_node
            if node.right:
                right_node = dfs(node.right)
                if right_node.val < node.val:
                    right = right_node


            right = dfs(node.right)

            return max([ll, lr, node.val]), min([rl, rr, node.val])


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def inorderTravese(node):
            if not node:
                return []
            return inorderTravese(node.left) + [node] + inorderTravese(node.right)

        lst = inorderTravese(root)
        drop = []
        for i in range(1, len(lst)):
            if lst[i].val < lst[i-1].val:
                drop.extend([lst[i-1], lst[i]])
        drop[0].val, drop[-1].val = drop[-1].val, drop[0].val
