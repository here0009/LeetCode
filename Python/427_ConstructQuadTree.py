"""
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:



Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

Example 3:

Input: grid = [[1,1],[1,1]]
Output: [[1,1]]
Example 4:

Input: grid = [[0]]
Output: [[1,0]]
Example 5:

Input: grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
Output: [[0,1],[1,1],[1,0],[1,0],[1,1]]
 

Constraints:

n == grid.length == grid[i].length
n == 2^x where 0 <= x <= 6
"""



# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid) -> 'Node':
        length = len(grid)
        if length == 1:
            return Node(grid[0][0], True, None, None, None, None)
        # if length == 0:
        #     return None
        half = length//2
        # print(half)
        isLeaf = False
        # for row in grid:
        #     print(row)
        # print(length)
        if half == 1:
            if grid[0][0] == grid[0][1] == grid[1][0] == grid[1][1]:
                isLeaf = True
            val = grid[0][0] or grid[0][1] or grid[1][0] or grid[1][1]
            topLeft = Node(grid[0][0], True, None, None, None, None)
            topRight = Node(grid[0][1], True, None, None, None, None)
            bottomLeft = Node(grid[1][0], True, None, None, None, None)
            bottomRight = Node(grid[1][1], True, None, None, None, None)
            # print(val, isLeaf)
            return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
        else:
            g1,g2,g3,g4 = [],[],[],[] #tl, tr, bl, br
            for i,row in enumerate(grid):
                if i < half:
                    g1.append(row[:half])
                    g2.append(row[half:])
                else:
                    g3.append(row[:half])
                    g4.append(row[half:])
            topLeft = self.construct(g1)
            topRight = self.construct(g2)
            bottomLeft = self.construct(g3)
            bottomRight = self.construct(g4)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
                if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                    isLeaf = True
            val = topLeft.val or topRight.val or bottomLeft.val or bottomRight.val
            res = Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
            print(res.val, res.isLeaf)
            return res

class Solution:
    def construct(self, grid) -> 'Node':
        length = len(grid)
        if length == 1:
            return Node(grid[0][0], True, None, None, None, None)
        half = length//2
        # print(half)
        isLeaf = False
        g1,g2,g3,g4 = [],[],[],[] #tl, tr, bl, br
        for i,row in enumerate(grid):
            if i < half:
                g1.append(row[:half])
                g2.append(row[half:])
            else:
                g3.append(row[:half])
                g4.append(row[half:])
        topLeft = self.construct(g1)
        topRight = self.construct(g2)
        bottomLeft = self.construct(g3)
        bottomRight = self.construct(g4)
        val = topLeft.val or topRight.val or bottomLeft.val or bottomRight.val
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
            if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                isLeaf = True
                return Node(val, True, None, None, None, None)
        res = Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
        # print(res.val, res.isLeaf)
        return res
        
# https://leetcode.com/problems/construct-quad-tree/discuss/148806/Python-short-and-readable-DFS-solution
class Solution:
    def construct(self, grid):
        def dfs(x, y, l):
            if l == 1:
                node = Node(grid[x][y] == 1, True, None, None, None, None)
            else:
                tLeft = dfs(x, y, l // 2)
                tRight = dfs(x, y + l // 2, l // 2)
                bLeft = dfs(x + l // 2, y, l// 2)
                bRight = dfs(x + l // 2, y + l // 2, l // 2)
                value = tLeft.val or tRight.val or bLeft.val or bRight.val
                if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                    node = Node(value, True, None, None, None, None)
                else:
                    node = Node(value, False, tLeft, tRight, bLeft, bRight)
            return node
        return grid and dfs(0, 0, len(grid)) or None

S = Solution()
grid = [[0, 1], [1, 0]]
S.construct(grid)
grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
S.construct(grid)
grid = [[1,1],[1,1]]
S.construct(grid)
grid = [[0]]
S.construct(grid)
grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
S.construct(grid)
grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
S.construct(grid)
# grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
# S.construct(grid)
