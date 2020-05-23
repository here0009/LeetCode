"""
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
 

Note:

The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.
"""
# Definition for a binary tree node.
from collections import deque
def Tree_Builds_BFS(node_val_list):
    node_q = deque()
    if node_val_list[0]:
        root = TreeNode(node_val_list[0])
        node_q.append(root)
    else:
        return None
    counts = 0 #counts for left and right
    for val in node_val_list[1:]:
        # print(val)
        if val is not None:
            node = TreeNode(val)
        else:
            node = None
        if node:
            node_q.append(node)
        tmp_node = node_q[0]
        if counts == 0:
            tmp_node.left = node
            counts = 1
        else:
            tmp_node.right = node
            node_q.popleft()
            counts = 0

    return root
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def sumRight(root):
            if not root:
                return 0
            sumRight(root.right)
            self.n += root.val 
            root.val = self.n
            sumRight(root.left)

        self.n = 0
        sumRight(root)
        return root


class Solution:
    def __init__(self):
        self.n = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return 0
        self.bstToGst(root.right)
        self.n += root.val 
        root.val = self.n
        self.bstToGst(root.left)

        return root


node_val_list = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
root = Tree_Builds_BFS(node_val_list)
print(root.val)
print(root.left.val)

s = Solution()
root = s.bstToGst(root)
print(root.val)
print(root.left.val)
print(root.right.left.val)
print(root.left.left.val)