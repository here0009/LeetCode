"""
Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

 

Example 1:



Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:



Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
 

Constraints:

Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-bsts
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def dfs(n1, n2):
            if not n1 or not n2 or self.res or (n1, n2) in visited:
                return
            visited.add((n1, n2))
            v = n1.val + n2.val
            if v == target:
                self.res = True
                return
            elif v > target:
                dfs(n1.left, n2)
                dfs(n1, n2.left)
            else:
                dfs(n1.right, n2)
                dfs(n1, n2.right)

        self.res = False
        visited = set()
        dfs(root1, root2)
        return self.res
