"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers modulo 10^9 + 7.

 

Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 

Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        self.res = 0
        M = 1e9 + 7
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                self.res += root.val
                return [0]
            if root.left:
                depth_list_left = [val+1 for val in dfs(root.left)]
            else:
                depth_list_left = []
            if root.right:
                depth_list_right = [val+1 for val in dfs(root.right)]
            depth_list = []
            depth_list = depth_list_left.extend(depth_list_right)
            if root.val:
                for depth in depth_list:
                    self.res += 2**depth
            self.res = self.res % M
            return depth_list

        dfs(root)
        return self.res

             
class Solution_1:
    """
    DFS can solve the problem.
    Use a variable total to represent the binary number corresponding to the path from the root to the parent of this node. When visit the children of this node, the number becomes total = total * 2 + node.val.
    If this node does not have any children, then it is the time to add the number total to the result self.sum.
    """
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def dfs(root, path_total):
            if not root:
                return
            path_total = int((2*path_total + root.val))%M
            if not root.left and not root.right:
                self.sum += path_total
            dfs(root.left,path_total)
            dfs(root.right,path_total)

        self.sum = 0
        M = 1e9+7
        dfs(root,0)
        return self.sum


class Solution_2:

    def sumRootToLeaf(self, root: TreeNode, val=0) -> int:
        if not root:
            return
        val = 2 * val + root.val
        if not root.left and not root.right:
            return val
        return self.sumRootToLeaf(root.left, root.val) + self.sumRootToLeaf(root.right, root.val) 

class Solution_1:
    """
    We recursively pass the current value of path to the children.
    If root == null, no value, return 0.
    If root != null,
    we double the value from its parent and add the node's value,
    like the process of transforming base 2 to base 10.

    In the end of recursion,
    if root.left == root.right == null,
    return the current val.


    Time Complexity:
    O(N) time, O(logN) for recursion.
    """
    def sumRootToLeaf(self, root, val=0):
        if not root: return 0
        val = (val * 2 + root.val) % (10**9 + 7)
        if not root.left and not root.right: 
            return val
        return (self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)) % (10**9 + 7)
