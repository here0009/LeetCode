"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \\       /     /      / \\      \
     3     2     1      1   3      2
    /     /       \\                 \
   2     1         2                 3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        def produceTrees(p,q):
            #produce trees that >=p and <q
            if p == q:
                return [None]
            res = []
            for i in range(p,q):
                root = TreeNode(i)
                left_trees = produceTrees(p,i)
                right_trees =produceTrees(i+1,q)
                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)
            return res
        if n == 0:
            return []
        return produceTrees(1,n+1)
