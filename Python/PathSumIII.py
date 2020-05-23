"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \\    \
  3   2   11
 / \\   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    wrong answer
    """
    def pathSum(self, root, sum_val: int) -> int:
        def dfs(root, vals):
            if root.val in vals:
                counter += 1
            vals.append(sum_va1 - root.val)
            if root.left and dfs(root.left, vals):
                counter += 1
            if root.right and dfs(root.right, remainder):
                counter += 1

        counter = 0
        dfs(root, sum_val)
        return counter

class Solution:
    def pathSum(self, root, val: int) -> int:
        def dfs(root,val):
            if not root:
                return
            rmd = val - root.val - sum(path)
            if rmd == 0:
                self.res += 1
            dfs(root.left, val)
            dfs(root.right, val)
            if rmd != val:
                dfs(root.left, rmd)
                dfs(root.right, rmd)

        self.res = 0
        dfs(root, val)
        return self.res


class Solution:
    def pathSum(self, root, val: int) -> int:
        def dfs(root,val):
            if not root:
                return
            dfs_withnode(root, val)
            dfs(root.left, val)
            dfs(root.right, val)

        def dfs_withnode(root,val):
            if not root:
                return
            if val == root.val:
                self.res += 1
            dfs_withnode(root.left, val-root.val)
            dfs_withnode(root.right, val-root.val)


        self.res = 0
        dfs(root, val)
        return self.res


class Solution:
    def pathSum(self, root, val: int) -> int:

        def dfs(root, val_list):