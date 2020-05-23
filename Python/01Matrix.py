"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""
import math
class Solution_1:
    def updateMatrix(self, matrix):
        def minDist(i,j):
            if res[i][j] is not None:
                return res[i][j]

            # print(i,j)
            r1 = r2 = r3 = r4 = math.inf
            if i-1 >= 0:
                r1 = 1+minDist(i-1,j)
            if i+1 < len_row:
                r2 = 1+minDist(i+1,j)
            if j-1 >= 0:
                r3 = 1+minDist(i,j-1)
            if j+1 < len_col:
                r4 = 1+minDist(i,j+1)
            k = [r for r in [r1,r2,r3,r4] if r > 0]
            return min(k)

        res = []
        len_row = len(matrix)
        len_col = len(matrix[0])
        for row in matrix:
            r =[]
            for cell in row:
                if cell == 0:
                    r.append(0)
                else:
                    r.append(None)
            res.append(r)

        for i in range(len_row):
            for j in range(len_col):
                if res[i][j] is None:
                    res[i][j] = minDist(i,j)

        return res

from collections import deque
class Solution:
    def updateMatrix(self, matrix):
        len_row = len(matrix)
        len_col = len(matrix[0])
        res = [[0]*len_col for i in range(len_row)]
        q = deque()
        for i in range(len_row):
            r =[]
            for j in range(len_col):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    q.append((i,j))
                else:
                    res[i][j] = math.inf
        # print(res)
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        while q:
            i,j = q.popleft()
            for delta_i, delta_j in directions:
                new_i, new_j = i+delta_i, j+delta_j
                if new_i >=0 and new_i < len_row and new_j >=0 and new_j < len_col:
                    if res[new_i][new_j] > 1 + res[i][j]:
                        res[new_i][new_j] = 1 + res[i][j]
                        q.append((new_i, new_j))
        return res
  


s = Solution()
matrix = [[0,0,0],[0,1,0],[0,0,0]]
print(s.updateMatrix(matrix))

matrix = [[0,0,0],[0,1,0],[1,1,1]]
print(s.updateMatrix(matrix))