# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        In this problem, one should compare the left and right subtree of  a root, but only got one root. use root.left and root.right will make the recursive process difficult, so we can compare root and root.
        """
        if not root:
            return True            
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        """
        :type tN1, tN2: TreeNode
        : rtype: bool
        """
        if left is None and right is None: #both of them do not exist
            return True
        elif left is None or right is None: #one of them do not exsit
            return False

        if left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(right.left, left.right)
            