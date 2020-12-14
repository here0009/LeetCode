"""
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

 

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
 

Your task is to collect maximum number of cherries possible by following the rules below:

 

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
 

 

Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
 

Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
"""


from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        wrong answer
        """
        def nxt_pos(i, j, sign):
            res = []
            for di, dj in [(0, 1), (1, 0)]:
                ni, nj = i + sign * di, j + sign * dj
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] != -1:
                    yield ni, nj

        def rev_dfs(i, j):
            if i == 0 and j == 0:
                return 0
            res = -float('inf')
            val = grid[i][j] == 1
            for ni, nj in nxt_pos(i, j, -1):
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    res = max(res, val + dfs(ni, nj))
                    visited[ni][nj] = 0
            return res

        def dfs(i, j):
            if i == N - 1 and j == N - 1:
                for _i in range(N):
                    for _j in range(N):
                        visited[_i][_j] = 0
                visited[i][j] = 1
                return rev_dfs(i, j)
            res = -float('inf')
            val = grid[i][j] == 1
            for ni, nj in nxt_pos(i, j, 1):
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    res = max(res, val + dfs(ni, nj))
                    visited[ni][nj] = 0
            return res

        N = len(grid)
        visited = [[0] * N for _ in range(N)]
        visited[0][0] = 1
        return dfs(0, 0)


from functools import lru_cache
class Solution:
    """
    Thoughts: 2 people pick cherries from 0,0 to N-1,N-1, return the max val
    """

    def cherryPickup(self, grid: List[List[int]]) -> int:
        def neighbors(r1, c1, r2, c2):
            for i, j, p, q in dir4:
                di, dj, dp, dq = r1 + i, c1 + j, r2 + p, c2 + q
                if 0 <= di < N and 0 <= dj < N and 0 <= dp < N and 0 <= dq < N:
                    yield di, dj, dp, dq

        @lru_cache(None)
        def dp(r1, c1, r2, c2):
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float('inf')
            if r1 == c1 == r2 == c2 == N - 1:
                return int(grid[N - 1][N - 1] == 1)
            if r1 == r2 and c1 == c2:
                curr = int(grid[r1][c1] == 1)
            else:
                curr = int(grid[r1][c1] == 1) + int(grid[r2][c2] == 1)
            res = max([dp(*lst) for lst in neighbors(r1, c1, r2, c2)])
            return curr + res

        N = len(grid)
        dir4 = [(0,1,0,1), (1,0,1,0), (0,1,1,0), (1,0,0,1)]
        res = dp(0, 0, 0, 0)
        return res if res != -float('inf') else 0

S = Solution()
grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
print(S.cherryPickup(grid))
grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
print(S.cherryPickup(grid))