"""
Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        bfs = [root]
        while len(bfs) > 0:
            bfs2 = []
            for node in bfs:
                if node.left:
                    bfs2.append(node.left)
                if node.right:
                    bfs2.append(node.right)
            if len(bfs2) == 0:
                return sum(node.val for node in bfs)
            bfs = bfs2

s = Solution()
print(s.deepestLeavesSum(root))
