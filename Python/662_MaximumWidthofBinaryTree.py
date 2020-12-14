"""
Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input: 

           1
         /   \
        3     2
       / \\     \\  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \\       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \\  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
 

Constraints:

The given binary tree will have between 1 and 3000 nodes.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """
        TLE
        """
        res = 1
        bfs = deque([root])
        while bfs:
            bfs2 = deque([])
            for node in bfs:
                if node:
                    bfs2.extend([node.left, node.right])
                else:
                    bfs2.extend([None, None])
            while bfs2 and bfs2[0] is None:
                bfs2.popleft()
            while bfs2 and bfs2[-1] is None:
                bfs2.pop()
            res = max(res, len(bfs2))
            bfs = bfs2
        return res



class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        bfs = [(0, root)]
        while bfs:
            bfs2 = []
            res = max(res, bfs[-1][0] - bfs[0][0] + 1)
            for v, node in bfs:
                if node.left:
                    bfs2.append((2*v, node.left))
                if node.right:
                    bfs2.append((2*v+1, node.right))
            bfs = bfs2
        return res