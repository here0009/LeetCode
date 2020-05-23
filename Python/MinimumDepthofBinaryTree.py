"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
# Definition for a binary tree node.

def Tree_Builds_BFS(node_val_list):
    node_list = []
    if not node_val_list:
        return None
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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':

        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

class Solution:
    """
    more elegant
    """
    def minDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        if not root.left or not root.right:
            return 1 + self.minDepth(root.left) + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

s = Solution()
node_val_list = [3,9,20,None,None,15,7]
root = Tree_Builds_BFS(node_val_list)
print(s.minDepth(root))

node_val_list = [3,9,20,5,6,15,7]
root = Tree_Builds_BFS(node_val_list)
print(s.minDepth(root))

node_val_list = [31]
root = Tree_Builds_BFS(node_val_list)
print(s.minDepth(root))

node_val_list = []
root = Tree_Builds_BFS(node_val_list)
print(s.minDepth(root))

node_val_list = [1,2]
root = Tree_Builds_BFS(node_val_list)
print(s.minDepth(root))

node_val_list = [1,2,3,4,None,None,5]
root = Tree_Builds_BFS(node_val_list)
print(s.minDepth(root))