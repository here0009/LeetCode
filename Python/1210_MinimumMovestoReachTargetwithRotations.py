"""
In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1). The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).

In one move the snake can:

Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).

Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty. In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return -1.

 

Example 1:



Input: grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
Output: 11
Explanation:
One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].
Example 2:

Input: grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
Output: 9
 

Constraints:

2 <= n <= 100
0 <= grid[i][j] <= 1
It is guaranteed that the snake starts at empty cells.
"""


from typing import List
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        """
        the snake can move in the direction perpendicular to its body...
        TLE
        """
        def inRange(i, j):
            return 0 <= i < N and 0 <= j < N

        def neighbors(i, j, direction):
            lst = []
            if direction == 0:
                if inRange(i + 1, j) and inRange(i + 1, j + 1) and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                    lst.append((i, j, 1 - direction))
                    lst.append((i + 1, j, direction))
                if inRange(i, j + 2) and grid[i][j + 2] == 0:
                    lst.append((i, j + 1, direction))
            else:
                if inRange(i, j + 1) and inRange(i + 1, j + 1) and grid[i][j + 1] == 0 and grid[i + 1][j + 1] == 0:
                    lst.append((i, j, 1 - direction))
                    lst.append((i, j + 1, direction))
                if inRange(i + 2, j) and grid[i + 2][j] == 0:
                    lst.append((i + 1, j, direction))
            return lst

        # @lru_cache(None)
        def dp(i, j, direction):
            """
            direction, 0 for horizontal, 1 for vertical
            """
            # print(i, j, direction)
            if i == N - 1 and j == N - 2 and direction == 0:  # reach the target
                return 0
            res = float('inf')
            for ni, nj, nd in neighbors(i, j, direction):
                if (ni, nj, nd) not in visited:
                    visited.add((ni, nj, nd))
                    res = min(res, 1 + dp(ni, nj, nd))
                    visited.remove((ni, nj, nd))
            return res

        N = len(grid)
        visited = set()
        visited.add(tuple([0, 0, 0]))
        res = dp(0, 0, 0)
        return res if res != float('inf') else -1


from typing import List
from collections import deque
class Solution_1:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        """
        the snake can move in the direction perpendicular to its body...
        """
        def inRange(i, j):
            return 0 <= i < N and 0 <= j < N

        N = len(grid)
        dq = deque([(0, 0, 0, 0)])  #i, j, direction, step
        target = (N - 1, N - 2, 0)
        visited = set()
        while dq:
            i, j, d, steps = dq.popleft()
            if (i, j, d) == target:
                return steps
            if (i, j, d) not in visited:
                visited.add((i, j, d))
                if d == 0:
                    if inRange(i + 1, j) and inRange(i + 1, j + 1) and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                        dq.append((i, j, 1 - d, steps + 1))  # rotate clockwise
                        dq.append((i + 1, j, d, steps + 1))  # down
                    if inRange(i, j + 2) and grid[i][j + 2] == 0:
                        dq.append((i, j + 1, d, steps + 1))  # right
                else:
                    if inRange(i, j + 1) and inRange(i + 1, j + 1) and grid[i][j + 1] == 0 and grid[i + 1][j + 1] == 0:
                        dq.append((i, j, 1 - d, steps + 1))  # rotate counterclockwise
                        dq.append((i, j + 1, d, steps + 1))  # right
                    if inRange(i + 2, j) and grid[i + 2][j] == 0:
                        dq.append((i + 1, j, d, steps + 1))  # down
        return -1


S = Solution()
grid = [[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]]
print(S.minimumMoves(grid))
grid = [[0,0,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,0]]
print(S.minimumMoves(grid))
