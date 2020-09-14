"""
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:

Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:

Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0,0), (1,1) and (2,2) are special positions. 
Example 3:

Input: mat = [[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]
Output: 2
Example 4:

Input: mat = [[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]]
Output: 3
 

Constraints:

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is 0 or 1.
"""


class Solution:
    def numSpecial(self, mat) -> int:
        m = len(mat)
        n = len(mat[0])
        sum_row = [0]*m
        sum_col = [0]*n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    sum_row[i] += 1
                    sum_col[j] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if sum_row[i] == sum_col[j] == 1:
                    res += mat[i][j] == 1
        return res

S = Solution()

mat = [[1,0,0],[0,0,1],[1,0,0]]
print(S.numSpecial(mat))
mat = [[1,0,0],[0,1,0],[0,0,1]]
print(S.numSpecial(mat))
mat = [[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]
print(S.numSpecial(mat))
mat = [[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
print(S.numSpecial(mat))
mat = [[0,0],[0,0],[1,0]]
print(S.numSpecial(mat))