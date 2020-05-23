"""
Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:



Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:



Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
Example 4:

Input: root = [1,1]
Output: 1
 

Constraints:

Each tree has at most 50000 nodes and at least 2 nodes.
Each node's value is between [1, 10000].
"""
# Definition for a binary tree node.
from LeetCode import Tree_Builds_BFS
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def maxProduct(self, root: TreeNode) -> int:
        def dfs_total(node):
            if node:
                return node.val + dfs_total(node.left) + dfs_total(node.right)
            else:
                return 0

        def dfs(node):
            if node:
                tmp = node.val + dfs(node.left) + dfs(node.right)
                # print(node.val, tmp, self.half)
                if tmp >= total/2 and self.flag:
                    self.flag = False
                    self.half = tmp
                return tmp
            else:
                return 0

        self.half = root.val
        total = dfs_total(root)
        # return total
        self.flag = True
        dfs(root)
        # print(total,self.half)
        if self.flag:
            return self.half * (total - self.half)
        else:
            left = dfs(root.left)
            right = total - root.val - left
            return max(left*(total-left), right*(total-right))



class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def dfs_total(node):
            if node:
                return node.val + dfs_total(node.left) + dfs_total(node.right)
            else:
                return 0

        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                self.res = max(self.res, left*(total-left), right*(total-right)) 
                return node.val + left + right
            else:
                return 0

        M = 10**9 + 7
        total = dfs_total(root)
        self.res = 0
        dfs(root)
        return self.res % M

S = Solution()
root = [1,2,3,4,5,6]
r = Tree_Builds_BFS(root)
print(S.maxProduct(r))

# root = [1,None,2,3,4,None,None,5,6]
# r = Tree_Builds_BFS(root)
# print(S.maxProduct(r))

root = [2,3,9,10,7,8,6,5,4,11,1]
r = Tree_Builds_BFS(root)
print(S.maxProduct(r))

root = [1,1]
r = Tree_Builds_BFS(root)
print(S.maxProduct(r))

root = [10,7,6,None,10,None,10]
r = Tree_Builds_BFS(root)
print(S.maxProduct(r))
# Output:
# 0
# Expected:
# 442