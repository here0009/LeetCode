"""
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
"""

from functools import lru_cache
class Solution:
    def swimInWater(self, grid) -> int:
        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        @lru_cache(None)
        def dfs(i,j):
            visited[i][j] = 1
            if i == R-1 and j == C-1:
                return grid[R-1][C-1]
            cost = float('inf')
            lst = sorted([(grid[i+di][j+dj], i+di, j+dj )for di,dj in directions if inRange(i+di, j+dj) and visited[i+di][j+dj] == 0])
            for _, ni,nj in lst:
                # visited[ni][nj] = 1
                cost = min(cost, dfs(ni, nj))
            return max(grid[i][j], cost)


        R, C = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[0]*C for _ in range(R)]
        # visited[0][0] = 1
        return dfs(0, 0) 

import heapq
class Solution:
    def swimInWater(self, grid) -> int:
        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (grid[0][0], 0, 0))
        R, C = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[0]*C for _ in range(R)]
        visited[0][0] = 1
        while pq:
            cost, i, j = heapq.heappop(pq)
            if i == R-1 and j == C-1:
                return cost
            for di,dj in directions:
                ni, nj = i+di, j+dj
                if inRange(ni,nj) and visited[ni][nj] == 0:
                    heapq.heappush(pq, (max(cost, grid[ni][nj]), ni, nj))
                    visited[ni][nj] = 1
        return float('inf')

class Solution:
    def swimInWater(self, grid) -> int:
        N = len(grid)
        l, r = grid[0][0], N*N-1
        
        def reachable(T):
            bfs = [(0,0)]
            seen = set((0,0))
            for i,j in bfs:
                if grid[i][j] <= T:
                    if i == j == N-1:
                        return True
                    for di,dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                        ni,nj = i+di, j+dj
                        if 0<=ni<N and 0<=nj<N and (ni,nj) not in seen:
                            seen.add((ni,nj))
                            bfs.append((ni,nj))
            return False

        while l < r:
            m = (l+r)//2
            if reachable(m):
                r = m
            else:
                l = m+1
        return r

class Solution:
    def swimInWater(self, grid) -> int:

        def find(pos):
            if pos != parents[pos]:
                parents[pos] = find(parents[pos])
            return parents[pos]

        def union(pos1, pos2):
            p1, p2 = find(pos1), find(pos2)
            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
            elif ranks[p2] > ranks[p1]:
                parents[p1] = p2
            else:
                parents[p2] = p1
                ranks[p1] += 1

        N = len(grid)
        table = {grid[i][j]:(i,j) for i in range(N) for j in range(N)}
        parents = {(i,j):(i,j) for i in range(N) for j in range(N)}
        ranks = {(i,j):0 for i in range(N) for j in range(N)}
        for t in range(N**2):
            r, c = table[t]
            for ri, ci in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0<=ri<N and 0<=ci<N and grid[ri][ci] <= t:
                    union((r,c), (ri, ci))
            if find((0,0)) == find((N-1, N-1)):
                return t
        return float('inf')



S = Solution()
grid = [[0,2],[1,3]]
print(S.swimInWater(grid))
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(S.swimInWater(grid))
grid = [[35,19,17,25,4,10],[8,18,29,21,28,31],[15,5,33,2,13,3],[26,20,27,23,11,1],[6,14,24,7,12,16],[30,34,32,22,0,9]]
print(S.swimInWater(grid))
grid = [[11,15,3,2],[6,4,0,13],[5,8,9,10],[1,14,12,7]]
print(S.swimInWater(grid))