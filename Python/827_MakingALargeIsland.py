"""
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Notes:

1 <= grid.length = grid[0].length <= 50.
0 <= grid[i][j] <= 1.
"""


from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def neigbors(i, j, directions):
            # print(i, j)
            for di, dj in directions:
                ni, nj = di + i, dj + j
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 1:
                    yield ni, nj

        def find(index):
            if root[index] != index:
                ri = find(root[index])
                root[index] = ri
            return root[index]

        def union(i, j):
            ri, rj = find(i), find(j)
            if ri == rj:
                return False
            root[rj] = ri
            size[ri] += size[rj]
            size[rj] = 0
            return True


        # i, j = divmod(index, N)

        N = len(grid)
        root = list(range(N * N))
        size = [0] * (N * N)
        dir2 = [(0, -1), (-1, 0)]  # union grid with its upper and left
        dir4 = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    size[i* N + j] = 1
                    for ni, nj in neigbors(i, j, dir2):
                        union((i * N + j), (ni * N + nj))
        # print(size)
        res = max(size)
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    tmp = set()
                    for ni, nj in neigbors(i, j, dir4):
                        tmp.add(find(ni * N + nj))
                    res = max(res, sum([size[k] for k in tmp] + [0]) + 1)
        return res

S = Solution()
grid = [[1, 0], [0, 1]]
print(S.largestIsland(grid))
grid = [[1, 1], [1, 0]]
print(S.largestIsland(grid))
grid = [[1, 1], [1, 1]]
print(S.largestIsland(grid))
