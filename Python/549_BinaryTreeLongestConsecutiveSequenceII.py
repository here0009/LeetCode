"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(node):
            """
            return val, max left bound and max right bound
            """
            nv, nmin, nmax = node.val, node.val, node.val
            if node.left:
                lv, lmin, lmax = dfs(node.left)
                if lv - nv == 1:
                    nmax = lmax
                elif nv - lv == 1:
                    nmin = lmin
            if node.right:
                rv, rmin, rmax = dfs(node.right)
                if rv - nv == 1:
                    nmax = max(nmax, rmax)
                elif nv - rv == 1:
                    nmin = min(nmin, rmin)
            self.res = max(self.res, nmax - nmin + 1)
            return nv, nmin, nmax

        self.res = 0
        if not root:
            return 0
        dfs(root)
        return self.res
            