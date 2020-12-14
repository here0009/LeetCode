"""You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

It is directly connected to the top of the grid, or
At least one other brick in its four adjacent cells is stable.
You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.

 

Example 1:

Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
Output: [2]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,1,1,0]]
The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].
Example 2:

Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,0,0]]
We erase the underlined brick at (1,1), resulting in the grid:
[[1,0,0,0],
 [1,0,0,0]]
All remaining bricks are still stable, so no bricks fall. The grid remains the same:
[[1,0,0,0],
 [1,0,0,0]]
Next, we erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,0,0,0]]
Once again, all remaining bricks are still stable, so no bricks fall.
Hence the result is [0,0].
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is 0 or 1.
1 <= hits.length <= 4 * 104
hits[i].length == 2
0 <= xi <= m - 1
0 <= yi <= n - 1
All (xi, yi) are unique.
"""


from typing import List
from collections import Counter, deque
class Solution:
    """
    wrong answer
    """
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def bfs(i,j):
            counts = 0
            dq = deque([(i,j)])
            print('hit', i, j)
            while dq:
                # print(dq)
                i,j = dq.popleft()
                if indegree[(i,j)] == 0:
                    grid[i][j] = 0
                    counts += 1
                for ni,nj in edges[(i,j)]:
                    indegree[(ni,nj)] -= 1
                    if grid[ni][nj] == 1:
                        dq.append((ni,nj))
            # print(edges)
            # print(indegree)
            return counts

        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        strength = Counter()
        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    for di,dj in dir4:
                        ni, nj = i+di, j+dj
                        if ni == -1 or (inRange(ni, nj) and grid[ni][nj] == 1):
                            strength[(i,j)] += 1
        for row in grid:
            print(row)
        print(strength)
        res = []
        for hit in hits:
            if grid[hit[0]][hit[1]] == 0:
                res.append(0)
                continue
            bfs = deque(tuple([hit]))
            print(bfs)
            counts = -1
            while bfs:
                i,j = bfs.popleft()
                grid[i][j] = 0
                strength[(i,j)] = 0
                counts += 1
                for di,dj in dir4:
                    ni,nj = i+di, j+dj
                    if inRange(ni,nj) and grid[ni][nj] == 1:
                        strength[(ni,nj)] -= 1
                        if strength[(ni,nj)] == 0:
                            bfs.append((ni,nj))
            res.append(counts)
        return res


from typing import List
from collections import Counter, deque, defaultdict
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        def dfs(i,j):
            for di,dj in dir4:
                ni,nj = i+di, j+dj
                if ni > 0 and inRange(ni,nj) and grid[ni][nj] == 1 and visited[ni][nj] == 0:
                    indegree[(ni,nj)] += 1
                    edges[(i,j)].append((ni,nj))
                    visited[ni][nj] = 1
                    dfs(ni,nj)
                    visited[ni][nj] = 0

        def remove(i,j):
            # print('rm',i,j)
            res = 0
            if indegree[(i,j)] == 0:
                grid[i][j] = 0
                res += 1

            for ni,nj in edges[(i,j)]:
                if grid[ni][nj] == 1 and visited[ni][nj] == 0:
                    indegree[(ni,nj)] -= 1
                    visited[ni][nj] = 1
                    res += remove(ni,nj)
                    visited[ni][nj] = 0
            if grid[i][j] == 0:
                del edges[(i,j)]
            return res

        

        indegree = Counter()
        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        edges = defaultdict(list)
        R, C = len(grid), len(grid[0])
        visited = [[0]*C for _ in range(R)]
        for j in range(C):
            if grid[0][j] == 1:
                visited[0][j] = 1
                dfs(0, j)

        for row in grid:
            print(row)
        # print(edges)
        # print(indegree)
        print(edges[(1,0)])
        res = []
        for hit in hits:
            i, j = hit
            # print('hit',i,j)
            if grid[i][j] == 0:
                res.append(0)
            else:
                indegree[(i,j)] = 0
                res.append(remove(i,j)-1)
            # print(edges)
            # print(indegree)

        return res

from typing import List
from collections import Counter, deque, defaultdict
class Solution:
    """
    try to refresh the grid after every hit, TLE
    """
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        def dfs(i,j):
            for di,dj in dir4:
                ni,nj = i+di, j+dj
                if ni > 0 and inRange(ni,nj) and grid[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    dfs(ni,nj)

        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        R, C = len(grid), len(grid[0])
        # for row in grid:
        #     print(row)
        score = sum(sum(row) for row in grid)

        res = []
        for hit in hits:
            i, j = hit
            # print('hit',i,j)
            if grid[i][j] == 0:
                res.append(0)
                continue
            grid[i][j] = 0
            visited = [[0]*C for _ in range(R)]
            for j in range(C):
                if grid[0][j] == 1:
                    visited[0][j] = 1
                    dfs(0, j)
            new_score = sum(sum(row) for row in visited)
            res.append(score - new_score - 1)
            grid = visited
            score = new_score
            # print('+++++++')
            # for row in grid:
            #     print(row)
        return res

"""
1. refresh the grid after all hits, mark the left bricks with 2. hitted brick will -1
2. all hit back, reversely. if a hit connect with a remaning brick (2), update the brick and the brick connected to it to 2. 
3. use dfs or union find to calculate the number added. and that is exactly the brick fall when you hit the brick.
"""

class DSU:
    def __init__(self, R, C):
        #R * C is the source, and isn't a grid square
        self.par = range(R*C + 1)
        self.rnk = [0] * (R*C + 1)
        self.sz = [1] * (R*C + 1)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]

    def size(self, x):
        return self.sz[self.find(x)]

    def top(self):
        # Size of component at ephemeral "source" node at index R*C,
        # minus 1 to not count the source itself in the size
        return self.size(len(self.sz) - 1) - 1

class Solution(object):
    def hitBricks(self, grid, hits):
        R, C = len(grid), len(grid[0])
        def index(r, c):
            return r * C + c

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        A = [row[:] for row in grid]
        for i, j in hits:
            A[i][j] = 0

        dsu = DSU(R, C)
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val:
                    i = index(r, c)
                    if r == 0:
                        dsu.union(i, R*C)
                    if r and A[r-1][c]:
                        dsu.union(i, index(r-1, c))
                    if c and A[r][c-1]:
                        dsu.union(i, index(r, c-1))

        ans = []
        for r, c in reversed(hits):
            pre_roof = dsu.top()
            if grid[r][c] == 0:
                ans.append(0)
            else:
                i = index(r, c)
                for nr, nc in neighbors(r, c):
                    if A[nr][nc]:
                        dsu.union(i, index(nr, nc))
                if r == 0:
                    dsu.union(i, R*C)
                A[r][c] = 1
                ans.append(max(0, dsu.top() - pre_roof - 1))
        return ans[::-1]


from typing import List
from collections import Counter, deque, defaultdict
class Solution:

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def neighbors(i,j):
            for di,dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni,nj = i+di, j+dj
                if 0 <= ni < R and 0 <= nj < C:
                    yield ni,nj

        def dfs(i, j):
            grid[i][j] = 2
            res = 1
            for ni,nj in neighbors(i,j):
                if grid[ni][nj] == 1:
                    res += dfs(ni,nj)
            return res

        R, C = len(grid), len(grid[0])

        res = []
        for i,j in hits:
            grid[i][j] -= 1

        for j in range(C):
            if grid[0][j] == 1:
                dfs(0, j)
        # print('+++++++')
        # for row in grid:
        #     print(row)
        res = []
        for i,j in hits[::-1]:
            grid[i][j] += 1
            if grid[i][j] == 1 and (i == 0 or any(grid[ni][nj] == 2 for ni,nj in neighbors(i,j))):
                res.append(dfs(i,j)-1)
            else:
                res.append(0)
            # print('+++++++')
            # for row in grid:
            #     print(row)
        # print('+++++++')
        return res[::-1]

S = Solution()
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
print(S.hitBricks(grid, hits))
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
print(S.hitBricks(grid, hits))
grid = [[1,0,1,0],[1,1,1,0]]
hits = [[1,0]]
print(S.hitBricks(grid, hits))
grid = [[1,0,1],[1,1,1]]
hits = [[0,0],[0,2],[1,1]]
print(S.hitBricks(grid, hits))
# Output
# [0,0,2]
# Expected
# [0,3,0]
grid = [[0,1,1,1,1],[1,1,1,1,0],[1,1,1,1,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
hits = [[6,0],[1,0]]
print(S.hitBricks(grid, hits))
# Output:
# [0,10,0,0,0,0,0,0,0,0,0]
# Expected:
# [0,0,0,0,0,0,0,0,0,0,0]