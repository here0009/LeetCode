"""
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

 

Example 1:


Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.
Example 2:


Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.
Example 3:


Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
Example 4:

Input: grid = [["O","*"],["#","O"]]
Output: 2
Example 5:

Input: grid = [["X","*"],["#","X"]]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[row][col] is '*', 'X', 'O', or '#'.
The grid contains exactly one '*'.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-to-get-food
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        def neighbors(i, j):
            for di, dj in dir4:
                ni, nj = i + di, j + dj
                if (ni, nj) not in visited and inRange(ni, nj) and grid[ni][nj] != 'X':
                    visited.add((ni, nj))
                    yield ni, nj

        R, C = len(grid), len(grid[0])
        dir4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        si, sj = None, None
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '*':
                    si, sj = i, j
                    break
        visited = set()
        visited.add((si, sj))
        bfs = [(si, sj, 0)]
        while bfs:
            bfs2 = []
            # print(bfs)
            for i, j, step in bfs:
                if grid[i][j] == '#':
                    return step
                for ni, nj in neighbors(i, j):
                    bfs2.append((ni, nj, step + 1))
            bfs = bfs2
        return -1

S = Solution()
grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
print(S.getFood(grid))
grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
print(S.getFood(grid))
grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
print(S.getFood(grid))
grid = [["O","*"],["#","O"]]
print(S.getFood(grid))
grid = [["X","*"],["#","X"]]
print(S.getFood(grid))
