"""
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
from LeetCode import Tree_Builds_BFS
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode):
        def sumSubTree(root):
            if not root:
                return 0
            val = root.val + sumSubTree(root.left) + sumSubTree(root.right)
            sums[val] = sums.get(val, 0) + 1
            return val


        res = []
        if not root:
            return res
        sums = dict()
        sumSubTree(root)
        # print(sums)
        max_val = max(sums.values())
        # keys = sorted(sums.keys(), key = lambda x: sums[x], reverse= True)
        return [key for key in sums.keys() if sums[key] == max_val]

s = Solution()
node_val_list = [5, 2, -3]
root = Tree_Builds_BFS(node_val_list)
# print(root.val)
# print(root.left.val)
print(s.findFrequentTreeSum(root))

node_val_list = [5, 2, -5]
root = Tree_Builds_BFS(node_val_list)
print(s.findFrequentTreeSum(root))

node_val_list = []
root = Tree_Builds_BFS(node_val_list)
print(s.findFrequentTreeSum(root))