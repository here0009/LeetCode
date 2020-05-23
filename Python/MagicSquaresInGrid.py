"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""
from collections import Counter
class Solution:
    def numMagicSquaresInside(self, grid) -> int:
        def checkMatrix(i,j):
            """
            check if a matrix is magic square with start index at i,j
            """
            # print(i,j)
            counter = Counter([grid[di][dj] for di in range(i,i+3) for dj in range(j,j+3)])
            for k in range(1,10):
                if counter[k] != 1:
                    return False

            rows_sum = [sum(grid[k][j:j+3]) for k in range(i,i+3)]
            # print(rows_sum)
            if not all(m == 15 for m in rows_sum):
                return False
            cols_sum = [sum(grid[q][k] for q in range(i,i+3)) for k in range(j,j+3)]
            # print(cols_sum)
            if not all(m == 15 for m in cols_sum):
                return False
            dgl_sum = sum(grid[i+k][j+k] for k in range(3))
            anti_dgl_sum = sum(grid[i+k][j+2-k] for k in range(3))
            # print(dgl_sum, anti_dgl_sum)
            if dgl_sum != 15 or anti_dgl_sum != 15:
                return False
            return True

        counts = 0
        m,n = len(grid), len(grid[0])
        for i in range(m-2):
            for j in range(n-2):
                counts += checkMatrix(i,j)
        return counts

S = Solution()
grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
print(S.numMagicSquaresInside(grid))
