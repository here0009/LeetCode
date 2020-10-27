"""
Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:
Input:     
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation: 
    5
   / 
  10
      
Sum: 15

   10
  /  \
 2    3

Sum: 15
Example 2:
Input:     
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
Note:
The range of tree node value is in the range of [-100000, 100000].
1 <= n <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/equal-tree-partition
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        def sumTree(node):
            if not node:
                return 0
            return node.val + sumTree(node.left) + sumTree(node.right)

        def dfs(node):
            if not node:
                return 0
            v = node.val + dfs(node.left) + dfs(node.right)
            if v == target and node is not root:  # if total is 0, then half is 0 too, so node can not be root
                self.res = True
            return v

        total = sumTree(root)
        target, rmd = divmod(total, 2)
        if rmd == 1:
            return False
        self.res = False
        dfs(root)
        return self.res


# 输入：
# [0,-1,1]
# 输出：
# true
# 预期结果：
# false

SyntaxError: invalid syntax
                                      ^
    if v == target and node is not root
Line 19  (Solution.py)