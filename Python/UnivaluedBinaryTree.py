"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 

Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false
 

Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if root:
                return root.val == value and dfs(root.left) and dfs(root.right)
            else:
                return True

        value = root.val
        return dfs(root)



# node_val_list = [3,9,20,None,None,15,7]

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

node_val_list = [1,1,1,1,1,None,1]
root = Tree_Builds_BFS(node_val_list)
print(root.val)
print(root.left.val)
# print(root.right.left.val)

node_val_list = [2,2,2,5,2]
root = Tree_Builds_BFS(node_val_list)
print(root.val)
print(root.left.val)

node_val_list = [2]
root = Tree_Builds_BFS(node_val_list)
print(root.val)

node_val_list = [None]
root = Tree_Builds_BFS(node_val_list)
print(root.val)

s = Solution()
print(s.isUnivalTree(root))