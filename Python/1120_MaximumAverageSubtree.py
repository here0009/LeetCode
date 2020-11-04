"""
Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

 

Example 1:



Input: [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
 

Note:

The number of nodes in the tree is between 1 and 5000.
Each node will have a value between 0 and 100000.
Answers will be accepted as correct if they are within 10^-5 of the correct answer.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-average-subtree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def dfs(node):
            """
            return the sum and counts
            """
            if not node:
                return 0, 0
            l_total, l_counts = dfs(node.left)
            r_total, r_counts = dfs(node.right)
            total = l_total + r_total + node.val
            counts = l_counts + r_counts + 1
            self.res = max(self.res, total/counts)
            return total, counts

        self.res = 0
        dfs(root)
        return self.res