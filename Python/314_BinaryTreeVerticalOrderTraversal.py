"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\\  /\
 /  \\/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\\  /\
 /  \\/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode):
        if not root:
            return []
        matrix = defaultdict(list)
        bfs = [(root, 0)]
        while bfs:
            bfs2 = []
            for node, index in bfs:
                matrix[index].append(node.val)
                if node.left:
                    bfs2.append((node.left, index-1))
                if node.right:
                    bfs2.append((node.right, index+1))
            bfs = bfs2
        keys = sorted(matrix.keys())
        return [matrix[key] for key in keys]
