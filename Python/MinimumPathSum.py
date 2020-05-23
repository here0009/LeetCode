"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
class Solution:
    def minPathSum(self, grid) -> int:
        m,n = len(grid), len(grid[0])
        matrix = [row[:] for row in grid]
        for i in range(1,n):
            matrix[0][i] += matrix[0][i-1]
        for j in range(1,m):
            matrix[j][0] += matrix[j-1][0]
        
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] += min(matrix[i][j-1], matrix[i-1][j])
        # for row in matrix:
        #     print (row)

        return matrix[m-1][n-1]

s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(s.minPathSum(grid))

