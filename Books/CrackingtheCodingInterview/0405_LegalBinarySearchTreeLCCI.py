"""
实现一个函数，检查一棵二叉树是否为二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true
示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/legal-binary-search-tree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return True, float('inf'), -float('inf')
            lflag, lmin, lmax = dfs(node.left)
            rlfag, rmin, rmax = dfs(node.right)
            if not lflag or not rlfag or node.val <= lmax or node.val >= rmin:
                return False, None, None
            return True, min(lmin, node.val), max(rmax, node.val)

        res, _, _ = dfs(root)
        return res