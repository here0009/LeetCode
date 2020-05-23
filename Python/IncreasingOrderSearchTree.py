"""
Given a binary search tree, rearrange the tree so that the minimum value in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \\   \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        global val_list
        val_list = []
        self.traverseBST(root, val_list)
        res_root = TreeNode(val_list[0])
        current_node = res_root
        if len(val_list) > 1:
            for value in val_list[1:]:
                tmp_node = TreeNode(value)
                current_node.left = None
                current_node.right = tmp_node
                current_node = tmp_node

        return res_root

    def traverseBST(self, root, value_list):
        if not root:
            return
        self.traverseBST(root.left, value_list)
        value_list.append(root.val)
        self.traverseBST(root.right, value_list)

tn = TreeNode(2)
tn.left = TreeNode(1)
tn.right = TreeNode(3)
print(tn.val)
s = Solution()
res = s.increasingBST(tn)
print(res.val, res.right.val, res.right.right.val)