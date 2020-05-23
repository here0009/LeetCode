"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        """
        Thoughts:
        Traverse the BST, LtR
        find L, record the list of the find pathway. Add all the node value and right subtree of node value until R
        """
        res = 0
        pathway = []
        self.findBST(root, L, pathway)
        pathway = reversed(pathway)
        for node in pathway:
            print(node.val)
            res += self.traverseBST_LtR(node, L, R, res)
        
        return self.traverseBST_LtR(root, L, R, 0)

    def findBST(self, root, value, pathway):
        if not root:
            return -1
        pathway.append(root)
        if value == root.val:
            return
        elif value < root.val:
            self.findBST(root.left, value, pathway)
        else:
            self.findBST(root.right, value, pathway)

    def traverseBST_LtR(self, root, L, R, res):
        if root:
            # res = self.traverseBST_LtR(root.left, L, R, res)
            if root.val >= L and root.val <= R:
                res += root.val
                print(root.val)
            else
            res += self.traverseBST_LtR(root.right, L, R, res)

        return res


def TreeInsertion(root, value):
    # print(value)
    if not root:
        return
    if value == None:
        return
    if value < root.val:
        if not root.left:
            root.left = TreeNode(value)
        else:
            TreeInsertion(root.left, value)
    elif value > root.val:
        if not root.right:
            root.right = TreeNode(value)
        else:
            TreeInsertion(root.right, value)
    else:
        return

# nodes = [10,5,15,3,7,13,18,1,None,6]
nodes = [10,5,15,3,7,None,18]
root = TreeNode(nodes[0])
# root_copy = root
for node in nodes:
    TreeInsertion(root, node)

# print(root.val)
# print(root.left.right.val)

s = Solution()
print(s.rangeSumBST(root, 7, 15))

class Solution_1:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        return self.inorder(root, 0, L, R)
            
    def inorder(self, root, value, L, R):
        if root:
            value = self.inorder(root.left, value, L, R)
            if root.val >= L and root.val <= R:
                value += root.val
            value = self.inorder(root.right, value, L, R)
        
        return value

# s = Solution_1()
# print(s.rangeSumBST(root, 7, 15))

class Solution_2:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.left, L, root.val) + self.rangeSumBST(root.right, root.val, R)

# s = Solution_2()
# print(s.rangeSumBST(root, 7, 15))