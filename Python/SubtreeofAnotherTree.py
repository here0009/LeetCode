# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from LeetCode import Tree_Builds_BFS
class Solution:
    def isEaqualTree(self,s, t):
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        return s.val == t.val and self.isEaqualTree(s.left, t.left) and self.isEaqualTree(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode):
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        return self.isEaqualTree(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right,t) 



S = Solution()
s = Tree_Builds_BFS([3,4,5,1,2])
t = Tree_Builds_BFS([4,1,2])
print(S.isEaqualTree(s,t))
print(S.isSubtree(s,t))

s = Tree_Builds_BFS([])
t = Tree_Builds_BFS([])
print(S.isEaqualTree(s,t))
print(S.isSubtree(s,t))