"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):

        def preInTree(pre_start, pre_end, in_start, in_end):
            if pre_start >= pre_end:
                return None
            root_num = preorder[pre_start]
            root_index = inorder.index(root_num)
            left_len = root_index-in_start
            right_len = in_end-(root_index+1)
            root = TreeNode(root_num)
            root.left = preInTree(pre_start+1, pre_start+1+left_len, in_start, root_index)
            root.right = preInTree(pre_end-right_len, pre_end, root_index+1, in_end)
            return root

        return preInTree(0,len(preorder),0,len(inorder))
