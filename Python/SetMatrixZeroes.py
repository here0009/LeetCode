"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution
"""
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        mul_rows = [1]*m
        mul_cols = [1]*n
        for i in range(m):
            tmp = 1
            for j in range(n):
                tmp *= matrix[i][j]
            mul_rows[i] = tmp

        for j in range(n):
            tmp = 1 
            for i in range(m):
                tmp *= matrix[i][j]
            mul_cols[j] = tmp
        # print(mul_cols)
        for i in range(m):
            if mul_rows[i] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(n):
            if mul_cols[j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        for row in matrix:
            print(row)

s = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(s.setZeroes(matrix))

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(s.setZeroes(matrix))
