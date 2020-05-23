"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
"""
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        noneFlag = False
        d = deque() 
        d.append(root)
        while d:
            tmpNode = d.popleft()
            # if tmpNode:
            #     print(tmpNode.val)
            # else:
            #     print("None")
            if tmpNode:
                if noneFlag:
                    return False
                d.append(tmpNode.left)
                d.append(tmpNode.right)
            else:
                noneFlag = True
        return True



def Tree_Builds_BFS(node_val_list):
    node_list = []
    for index, val in enumerate(node_val_list):
        if val:
            node = TreeNode(val)
            # print(val)
        else:
            node = None
        if index == 0:
            root = node
            node_list.append(root)
        else:

            if index%2:
                tmp = node_list[index//2]
                tmp.left = node
            else:
                tmp = node_list[index//2-1]
                tmp.right = node
            node_list.append(node)
    return root

s = Solution()

node_val_list = [1,2,3,4,5,6]
root = Tree_Builds_BFS(node_val_list)
# print(root.val)
# print(root.left.val)
# print(root.right.left.val)
print(s.isCompleteTree(root))


node_val_list = [1,2,3,4,5,None,7]
root = Tree_Builds_BFS(node_val_list)
# print(root.val)
# print(root.left.val)
# print(root.right.left.val)
print(s.isCompleteTree(root))