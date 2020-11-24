"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note:

There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return float('inf'), float('-inf')
            ll, lr = dfs(node.left)
            rl, rr = dfs(node.right)
            self.res = min([self.res, node.val - lr, rl - node.val])
            return min(node.val, ll), max(node.val, rr)

        self.res = float('inf')
        dfs(root)
        return self.res


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.pre is not None:
                self.res = min(self.res, node.val - self.pre)
            self.pre = node.val
            dfs(node.right)

        self.pre = None
        self.res = float('inf')
        dfs(root)
        return self.res