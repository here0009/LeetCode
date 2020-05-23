"""
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \\   \\  
      5   3   9 
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            tmp = []
            res.append(max([r.val for r in stack]))
            for r in stack:
                if r.left:
                    tmp.append(r.left)
                if r.right:
                    tmp.append(r.right)
            stack = tmp
        return res

s = Solution()
print(s.largestValues(root))
            
