"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res  = 0
        def dfs(root):
            if root:
                if root.left and not root.left.left and not root.left.right:
                    self.res += root.left.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.res

node_val_list = [3,9,20,None,None,15,7]
def Tree_Builds_BFS(node_val_list):
    if len(node_val_list) == 0:
        return None
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

root = Tree_Builds_BFS(node_val_list)
print(root.val)
print(root.left.val)
print(root.right.left.val)
# for index, node in enumerate(node_list):
#     if node:
#         print(index, node.val)

s = Solution()
print(s.sumOfLeftLeaves(root))
print(s.sumOfLeftLeaves(None))

root_2 = Tree_Builds_BFS([1,2,3,4,5])
print(root_2.val)
print(s.sumOfLeftLeaves(root_2))