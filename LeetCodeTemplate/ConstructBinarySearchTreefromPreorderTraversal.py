"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        def insertNode(root,val):
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    insertNode(root.left,val)
            elif val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    insertNode(root.right,val)

        if not preorder:
            return None
        root = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            insertNode(root, preorder[i])
        return root

s = Solution()
preorder = [8,5,1,7,10,12]
print(s.bstFromPreorder(preorder).val)
print(s.bstFromPreorder(preorder).left.val)
print(s.bstFromPreorder(preorder).right.right.val)
# preorder = []
# print(s.bstFromPreorder(preorder).val)