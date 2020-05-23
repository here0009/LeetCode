"""
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

 

Example 1:



Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 

Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        """
        Thougths:
        either substitue TreeNode val with max(node.val, node.left.val, node.right.val) or min(node.val, node.left.val, node.right.val)
        """
        self.res = 0
        def maxsub(root):
            tmp_max = root.val
            if root.left:
                root.left = maxsub(root.left)
                self.res = max(self.res, abs(root.val-root.left.val))
                tmp_max = max(root.val, root.left.val)
            if root.right:
                root.right = maxsub(root.right)
                self.res = max(self.res, abs(root.val-root.right.val))
                tmp_max = max(root.val, root.right.val) 
            root.val = tmp_max
            return root


        def minsub(root):
            tmp_min = root.val
            if root.left:
                root.left = minsub(root.left)
                self.res = min(self.res, abs(root.val-root.left.val))
                tmp_min = min(root.val, root.left.val)
            if root.right:
                root.right = minsub(root.right)
                self.res = min(self.res, abs(root.val-root.right.val))
                tmp_min = min(root.val, root.right.val)
            root.val = tmp_min
            return root

        maxsub(root)
        minsub(root)
        return self.res

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.max = 0
        def helper(node, nmin,nmax):
            if node is None:
                return
            self.max = max(self.max, abs(node.val-nmin), abs(node.val-nmax))
            nmin = min(nmin, node.val)
            nmax = max(nmax, node.val)
            helper(node.left, nmin, nmax)
            helper(node.right, nmin, nmax)

        helper(root, root.val, root.val)

        return self.max




from collections import deque
def Tree_Builds_BFS(node_val_list):
    node_q = deque()
    if node_val_list[0]:
        root = TreeNode(node_val_list[0])
        node_q.append(root)
    else:
        return None
    counts = 0 #counts for left and right
    for val in node_val_list[1:]:
        # print(val)
        if val is not None:
            node = TreeNode(val)
        else:
            node = None
        if node:
            node_q.append(node)
        tmp_node = node_q[0]
        if counts == 0:
            tmp_node.left = node
            counts = 1
        else:
            tmp_node.right = node
            node_q.popleft()
            counts = 0

    return root

node_val_list = [8,3,10,1,6,None,14,None,None,4,7,13]
root = Tree_Builds_BFS(node_val_list)
print(root.right.right.left.val)
s = Solution()
print(s.maxAncestorDiff(root))