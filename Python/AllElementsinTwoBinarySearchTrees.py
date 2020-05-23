"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1, root2):
        def inOrderTraverse(node, nums):
            if node:
                inOrderTraverse(node.left,nums)
                nums.append(node.val)
                inOrderTraverse(node.right,nums)
        l1 = []
        l2 = []
        inOrderTraverse(root1,l1)
        inOrderTraverse(root2,l2)
        print(l1)
        print(l2)
        l1_index,l2_index = 0,0
        l1_len,l2_len = len(l1), len(l2)
        res = []
        while l1_index < l1_len and l2_index < l2_len:
            if l1[l1_index] <= l2[l2_index]:
                res.append(l1[l1_index])
                l1_index += 1
            else:
                res.append(l2[l2_index])
                l2_index += 1
        if l1_index < l1_len:
            res.extend(l1[l1_index:])
        if l2_index < l2_len:
            res.extend(l2[l2_index:])
        return res


            