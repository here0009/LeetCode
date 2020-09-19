"""
Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode):
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        row = depth(root)
        col = 2**row-1
        i = 0
        j = 2**(row-1)-1
        res = [['']*col for _ in range(row)]
        bfs = [(root, i, j)]
        while bfs:
            bfs2 = []
            for node, i, j in bfs:
                res[i][j] = str(node.val)
                if node.left:
                    bfs2.append((node.left, i+1, j-2**(row-i-2)))
                if node.right:
                    bfs2.append((node.right, i+1, j+2**(row-i-2)))
            bfs = bfs2
        return res

class Solution:
    def printTree(self, root: TreeNode):
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        def update_output(node, row, left, right):
            if not node:
                return
            mid = (left + right)//2
            self.output[row][mid] = str(node.val)
            update_output(node.left, row+1, left, mid-1)
            update_output(node.right, row+1, mid+1, right)

        height = depth(root)
        width = 2**height-1
        self.output = [['']*width for _ in range(height)]
        update_output(root, 0, 0, width-1)
        return self.output


