"""
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

 

Note:

1 <= N <= 20
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N: int):
        if N == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1,N-1,2):
            left_list = self.allPossibleFBT(i)
            right_list = self.allPossibleFBT(N-i-1)
            for l in left_list:
                for r in right_list:
                    node = TreeNode(0)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res