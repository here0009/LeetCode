"""
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

Example 1:

Input: root1 = [1,2,3,4,5,6,None,None,None,7,8], root2 = [1,3,2,None,6,4,5,None,None,None,None,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram
 

Note:

Each tree will have at most 100 nodes.
Each value in each tree will be a unique integer in the range [0, 99].
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        """
        Thoughts:
        这个方法没有left和right子树为None的情况进行对比会出现问题.
        """

        if not self.isEqualNode(root1, root2):
            return False

        
        if not self.isEqualNode(root1.left, root2.left):
            root1.left, root1.right = root1.right, root1.left

        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)

    def isEqualNode(self, root1, root2):
        """
        return True if root1.val == root2.val
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            print(root1.val, root2.val)
            return True
        else:
            print(root1.val, root2.val)
            return False

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        """
        Thoughts:
        将判断部分和return部分分开, 在return部分通过分支进行判断
        """
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (not root2 and root1) or (root1.val != root2.val):
            return False
        print(root1.val, root2.val)
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)) 

s = Solution()

root1_list = [1,2,3,4,5,6,None,None,None,7,8]
root2_list = [1,3,2,None,6,4,5,None,None,None,None,8,7]
def Tree_Builds_BFS(node_val_list):
    node_list = []
    for index, val in enumerate(node_val_list):
        if val:
            node = TreeNode(val)
        else:
            node = None
        if index == 0:
            root = node
            node_list.append(root)
        else:
            if index%2:
                tmp = node_list[index//2]
                if tmp: #tmp is not None
                    tmp.left = node
            else:
                tmp = node_list[index//2-1]
                if tmp: #tmp is not None
                    tmp.right = node
            node_list.append(node)
    return root

root1 = Tree_Builds_BFS(root1_list)
print(root1.val)
print(root1.left.val)
print(root1.right.left.val)

root2 = Tree_Builds_BFS(root2_list)
print(root2.val)
print(root2.left.val)
print(root2.right.left.val)

s = Solution()
print(s.flipEquiv(root1, root2))