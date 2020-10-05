"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence
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
            return increasing depth and decreasing depth
            """
            if not node:
                return 0,0
            i, d = [1], [1]
            if node.left:
                li, ld = dfs(node.left)
                if node.val - node.left.val == 1:
                    i.append(li+1)
                elif node.val - node.left.val == -1:
                    d.append(ld+1)
            if node.right:
                ri, rd = dfs(node.right)
                if node.val - node.right.val == 1:
                    i.append(ri+1)
                elif node.val - node.right.val == -1:
                    d.append(rd+1)
            res_i, res_d = max(i), max(d)
            self.res = max(res_i, res_d, self.res)
            return res_i, res_d

        self.res = 0
        dfs(root)
        return self.res


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(node):
            """
            return the increasing depth, node val
            """
            if not node:
                return 0, float('inf')
            ld, lv = dfs(node.left)
            rd, rv = dfs(node.right)
            res_d, res_v = 1, node.val
            if lv - node.val == 1:
                res_d = max(res_d, ld+1)
            if rv - node.val == 1:
                res_d = max(res_d, rd+1)
            self.res = max(self.res, res_d)
            return res_d, res_v

        self.res = 0
        dfs(root)
        return self.res


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        """
        wrong answer,  it is the same as previous one,  do not know why
        """
        def dfs(node):
            """
            return the increasing depth, node val
            """
            if not node:
                return 0, float('inf')
            ld, lv = dfs(node.left)
            rd, rv = dfs(node.right)
            if lv - node.val == 1:
                ld += 1
            if rv - node.val == 1:
                rd += 1
            # ld += (lv - node.val == 1)
            # rd += (rv - node.val == 1)
            res_d = max([ld, rd, 1])
            self.res = max(self.res, res_d)
            return res_d, node.val

        self.res = 0
        dfs(root)
        return self.res


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(node, parent, length):
            if not node:
                return
            if parent != None and node.val == parent.val + 1:
                length += 1
            else:
                length = 1
            self.res = max(self.res, length)
            dfs(node.left, node, length)
            dfs(node.right, node, length)

        self.res = 0
        dfs(root, None, 0)
        return self.res