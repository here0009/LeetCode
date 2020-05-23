"""
Given a 2D grid of size n * m and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] becomes at grid[i][j + 1].
Element at grid[i][m - 1] becomes at grid[i + 1][0].
Element at grid[n - 1][m - 1] becomes at grid[0][0].
Return the 2D grid after applying shift operation k times.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
 

Constraints:

1 <= grid.length <= 50
1 <= grid[i].length <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
"""
"""
Thoughts:
shift the row order of last k col, then shift all the cols with col_num%k
"""
class Solution:
    def shiftGrid(self, grid, k: int):
        
        m, n = len(grid), len(grid[0])
        res = [row[:] for row in grid]
        #shift the rows of the last k col
        row_shifits, col_index = 0, n
        while row_shifits < k:
            col_index -= 1
            j = col_index%n
            tmp = res[m-1][j]
            for i in range(m-1,0,-1):
                res[i][j] = res[i-1][j]
            res[0][j] = tmp
            row_shifits += 1
        # for row in res:
        #     print(row)
        # print("++++++++++++")
        #shift cols
        # col_shifts = k%n
        res2 = [row[:] for row in res]
        for i in range(m):
            for j in range(n):
                shift_j = (j-k)%n
                res2[i][j] = res[i][shift_j]
        # for row in res2:
        #     print(row)
        # print("++++++++++++")
        return res2

s = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(s.shiftGrid(grid, k))

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(s.shiftGrid(grid, k))

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 9
print(s.shiftGrid(grid, k))