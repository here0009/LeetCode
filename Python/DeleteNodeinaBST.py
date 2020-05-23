"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \\   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \\   \
    4   7
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    replace the key node with its the most right node of left subtree, or the most left node of right subtree
    """
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def dfs(node, parent, flag):
            if node.val == key:
                if flag == 0:
                    parent.left = 

        def leftsubtree(node):
            if node
                if node.right:
                    return leftsubtree(node.right)
                else:
                    return node
            else:
                return node
            

        dummy = TreeNode(0)
        dummy.left = root
        dfs(dummy, root, 0) #0 for left, 1 for right
        return dummy.left


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        wrong answer
        """
        def dfs(node):
            if not node:
                return None
            if node:
                if key > node.val:
                    node.right = dfs(node.right)
                elif key < node.val:
                    node.left = dfs(node.left)
                else:
                    #substitue node with max value in left subtree or min value in right subtree
                    if node.left:
                        if not node.left.right:
                            return node.left
                        else:
                            tmp_node = node.left
                            while tmp_node.right:
                                tmp_node = tmp_node.right
                            new_root = tmp_node.right
                            new_root.left = node.left.left
                            new_root.right = node.left.right
                            return new_root
                    else:
                        return node.right

        
        return dfs(root)
"""
https://leetcode.com/problems/delete-node-in-a-bst/discuss/213685/Clean-Python-3-with-comments-in-details
"""
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left: #replace root with root.right
                return root.right
            else:
                tmp = root.left
                while tmp.right: #largest value in root.left subtree to replace root
                    tmp = tmp.right
                root.val = tmp.val
                root.left = self.deleteNode(root.left, tmp.val)
        return root