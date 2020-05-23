"""
1161. Maximum Level Sum of a Binary Tree
User Accepted:2594
User Tried:2667
Total Accepted:2633
Total Submissions:3626
Difficulty:Medium
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 

Example 1:



Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
 

Note:

The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxLevelSum(self, root) -> int:
        val_sum = root.val
        bfs = [root]
        level = 1
        res = 1
        while len(bfs) > 0:
            tmp = sum([node.val for node in bfs])
            if tmp > val_sum:
                res = level
                val_sum = tmp
            bfs_2 = []
            for node in bfs:
                if node.left:
                    bfs_2.append(node.left)
                if node.right:
                    bfs_2.append(node.right)
            bfs = bfs_2
            level += 1
        return res
            