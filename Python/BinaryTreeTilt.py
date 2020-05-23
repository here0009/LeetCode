"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumSubTree(root):
            """
            return the sum of a substree
            """
            if not root:
                return 0
            left = sumSubTree(root.left)
            right = sumSubTree(root.right)
            self.res += abs(left - right)
            return root.val + left + right

        if not root:
            return 0
        self.res = 0
        left = sumSubTree(root.left)
        right = sumSubTree(root.right)
        self.res += abs(left - right )
        
        return self.res

def Tree_Builds_BFS(node_val_list):
    if not node_val_list:
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

s = Solution()

# node_val_list = [1,2,3]
# root = Tree_Builds_BFS(node_val_list)
# print(s.findTilt(root))
# print(root.val)
# print(root.left.val)
node_val_list = [3,9,20,None,None,15,7]
root = Tree_Builds_BFS(node_val_list)
print(s.findTilt(root))

node_val_list = []
root = Tree_Builds_BFS(node_val_list)
print(s.findTilt(root))