"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10

Example 2:

Input: [[1,2],[3,4]]
Output: 34

Example 3:

Input: [[1,0],[0,2]]
Output: 16

Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 

Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
"""
class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        res = 0
        if N == 1:
            return 2 + 4*grid[0][0]
        #outer surface
        for i in range(N):
            res += grid[0][i] + grid[-1][i] + grid[i][0] + grid[i][-1]
        # print(res)


        #inner surface
        for i in range(0, N):
            for j in range(0, N):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    res += abs(grid[0][j] - grid[0][j-1])
                elif j == 0:
                    res += abs(grid[i][0] - grid[i-1][0])
                else:
                    res += abs(grid[i][j] - grid[i-1][j]) + abs(grid[i][j] - grid[i][j-1])
        # print(res)

        for i in range(N):
            for j in range(N):
                if grid[i][j] != 0:
                    res += 2
        # print(res)

        return res

"""
Do not seperate inner surface and out surface, for a small tower grid[i][j].
Its surface area is 2+4*v, 
besides, the hidden area can be calculated by minus 2*min(grid[i][j], gird[i-1][j]) and 2*min(grid[i][j], gird[i][j-1])
"""

class Solution_1:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        res = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    res += 2 + 4*grid[i][j]
                if i:
                    res -= 2*min(grid[i][j], grid[i-1][j])
                if j:
                    res -= 2*min(grid[i][j], grid[i][j-1])
        return res




s = Solution_1()
test = [[2]]
print(s.surfaceArea(test))
test = [[1,2],[3,4]]
print(s.surfaceArea(test))
test = [[1,0],[0,2]]
print(s.surfaceArea(test))
test = [[1,1,1],[1,0,1],[1,1,1]]
print(s.surfaceArea(test))
test = [[2,2,2],[2,1,2],[2,2,2]]
print(s.surfaceArea(test))


