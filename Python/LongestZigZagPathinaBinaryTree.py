"""
Given a binary tree root, a ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right then move to the right child of the current node otherwise move to the left child.
Change the direction from right to left or right to left.
Repeat the second and third step until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:



Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:



Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
 

Constraints:

Each tree has at most 50000 nodes..
Each node's value is between [1, 100].
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from functools import lru_cache
class Solution_1:
    def longestZigZag(self, root: TreeNode) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dfs(node,direction):
            """
            direction the node from its parent, -1 for left, 1 for right
            """
            if node is None:
                return 0
            elif direction == -1:
                return 1+dfs(node.right,1)
            elif direction == 1:
                return 1+dfs(node.left,-1)

        if not root:
            return 0
        return max(self.longestZigZag(root.left), self.longestZigZag(root.right), dfs(root.left,-1), dfs(root.right,1))

from collections import deque
class Solution_2:
    """
    BFS
    """
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        res = 0
        if root.left:
            q.append((root.left, 'l', 1))
        if root.right:
            q.append((root.right, 'r',1))
        while q:
            node, direction, counts = q.popleft()
            # print(node.val)
            res = max(res, counts)
            if node.left:
                if direction == 'l':
                    q.append((node.left, 'l', 1))
                else:
                    q.append((node.left, 'l', counts+1))
            if node.right:
                if direction == 'l':
                    q.append((node.right, 'r', counts+1))
                else:
                    q.append((node.right, 'r',1))
        # print('res',res)
        return res

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        @lru_cache(None)
        def dfs(node):
            """
            direction the node from its parent, -1 for left, 1 for right
            """
            if node is None:
                return [-1,-1,-1]
            left,right = dfs(node.left), dfs(node.right)
            return [left[1]+1, right[0]+1, max(left[1]+1, right[0]+1, left[2], right[2])]
            #left[1]+1 for node.left.right
            #left[1]+1 for node.right.left

        return dfs(root)[2]

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0,0
            #return the max value of node.left and node.right
            ll,lr = dfs(node.left)
            rl,rr = dfs(node.right)
            self.res = max(self.res, lr+1, rl+1)
            return lr+1, rl+1 

        self.res = 0
        dfs(root)
        return self.res-1


S = Solution()



from LeetCode import construcTree
from LeetCode import printBinaryTree
root = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1,None,1]
root = construcTree(root)
print(S.longestZigZag(root))

root = [1,1,1,None,1,None,None,1,1,None,1]
root = construcTree(root)
print(S.longestZigZag(root))

root = [1]
root = construcTree(root)
print(S.longestZigZag(root))

root = [1,1,1,1,1,1,1,None,None,None,None,None,None,1,1,None,None,1]
root = construcTree(root)
print(S.longestZigZag(root))
