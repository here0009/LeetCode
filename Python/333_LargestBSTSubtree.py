"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \\ 
  5  15 
 / \\   \\ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-bst-subtree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            """
            return isBST, size of subtree, min val in subtree, max val in subtree
            """
            if not node:
                return True, 0, float('inf'), -float('inf')
            left_BST, left_size, left_min, left_max = dfs(node.left)
            right_BST, right_size, right_min, right_max = dfs(node.right)
            node_min = min(left_min, right_min, node.val)
            node_max = max(left_max, right_max, node.val)
            if node.val <= left_max or node.val >= right_min or not (left_BST and right_BST):
                return False, 1, node_min, node_max
            else:
                res = 1+left_size+right_size
                self.res = max(self.res, res)
                return True, res, node_min, node_max

        if not root:
            return 0
        self.res = 1
        dfs(root)
        return self.res