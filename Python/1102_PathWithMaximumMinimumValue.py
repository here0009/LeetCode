"""
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

 

Example 1:



Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 
Example 2:



Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:



Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
 

Note:

1 <= R, C <= 100
0 <= A[i][j] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-with-maximum-minimum-value
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 作者：smoon1989
# 链接：https://leetcode-cn.com/problems/path-with-maximum-minimum-value/solution/pai-xu-bing-cha-ji-python3-by-smoon1989-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from  typing import List
class DSU(object):
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.sz = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R = len(A)
        C = len(A[0])
        n = R * C
        d = DSU(n)
        s = set()
        points = []
        for i in range(R):
            for j in range(C):
                points.append((A[i][j], i, j))
        points.sort()
        ans = min(A[0][0], A[R - 1][C - 1])
        s.add((0, 0))
        s.add((R - 1, C - 1))
        while d.find(0) != d.find(n - 1):
            p, x, y = points.pop()
            ans = min(ans, p)
            for i, j in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if (i, j) in s:
                    d.union(x * C + y, i * C + j)
                s.add((x, y))
        return ans



import heapq
class Solution:
    def maximumMinimumPath(self, A) -> int:
        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        R, C = len(A), len(A[0])
        pq = [(-A[0][0], 0, 0)]
        dp = [[-1]*C for _ in range(R)]
        dir4 = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(R):
            dp.append(A[i][:])
        while pq:
            val, i, j = heapq.heappop(pq)
            # print(pq)
            if i == R-1 and j == C-1:
                return -val
            for di, dj in dir4:
                ni, nj = i+di, j+dj
                if inRange(ni, nj):
                    tmp = min(A[ni][nj], -val)
                    if tmp > dp[ni][nj]:
                        dp[ni][nj] = tmp
                        heapq.heappush(pq, (-tmp, ni, nj))
        return None

S = Solution()
A = [[5,4,5],[1,2,6],[7,4,6]]
print(S.maximumMinimumPath(A))

A = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
print(S.maximumMinimumPath(A))
A = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
print(S.maximumMinimumPath(A))

A = [[0,1,0,0,1],[1,1,0,0,0],[1,0,1,1,1],[1,0,1,0,1],[1,0,1,0,1]]
print(S.maximumMinimumPath(A))