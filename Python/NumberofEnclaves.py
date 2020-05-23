"""
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
 

Note:

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
"""
class Solution:
    def numEnclaves(self, A) -> int:
        def expand(off_sea_set,i,j):
            ajacent_list = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            row, col = len(A), len(A[0])
            for r,c in ajacent_list:
                if (r,c) not in off_sea_set:
                    if r>0 and r< row and c>0 and c<col and A[r][c] == 1:
                        off_sea_set.add((r,c))
                        expand(off_sea_set,r,c)
            return 0

        land_sum = sum([sum(r) for r in A])
        row,col = len(A), len(A[0])
        off_sea = set()
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    if (i == 0 or i == row-1 or j == 0 or j == col-1):
                        off_sea.add((i,j))
                        expand(off_sea,i,j)
        # print(off_sea)
        return land_sum - len(off_sea)

s = Solution()
A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(s.numEnclaves(A))

A = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(s.numEnclaves(A))

A = [[1,1,1,1]]
print(s.numEnclaves(A))