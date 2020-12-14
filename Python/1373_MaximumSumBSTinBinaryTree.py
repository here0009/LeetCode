"""
Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
Example 2:



Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
Example 4:

Input: root = [2,1,3]
Output: 6
Example 5:

Input: root = [5,4,8,3,null,6,3]
Output: 7
 

Constraints:

The given binary tree will have between 1 and 40000 nodes.
Each node's value is between [-4 * 10^4 , 4 * 10^4].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return True, 0, float('inf'), -float('inf')
            v = node.val
            l_flag, l_sum, l_min, l_max = dfs(node.left)
            r_flag, r_sum, r_min, r_max = dfs(node.right)
            flag = True
            if (node.left and v <= l_max) or (node.right and v >= r_min):
                flag = False
            t_sum = l_sum + r_sum + v
            t_min = min(l_min, r_min, v)
            t_max = max(l_max, r_max, v)
            flag &= l_flag and r_flag
            if flag:
                print(node.val, t_sum)
                self.res = max(self.res, t_sum)
            return flag, t_sum, t_min, t_max
            # else:
            #     return False, t_sum, t_min, t_max

        self.res = 0
        dfs(root)
        return self.res

S = Solution()
print(S.maxSumBST(root))

# Input
# [4,8,null,6,1,9,null,-5,4,null,null,null,-3,null,10]
# Output
# 15
# Expected
# 14