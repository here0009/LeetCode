"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""


from functools import lru_cache
class Solution_2:
    def minimumEffortPath(self, heights) -> int:
        """
        wrong answer
        """
        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        def dfs(i,j,h):
            print(i,j,h)
            visited[i][j] = 1
            if i == R-1 and j == C-1:
                self.res = min(self.res, h)
                return
            h_min = float('inf')
            candidates = []
            for di,dj in dir4:
                ni,nj = i+di, j+dj
                if inRange(ni, nj) and visited[ni][nj] == 0:
                    diff = abs(heights[ni][nj] - heights[i][j])
                    h_min = min(diff, h_min)
                    candidates.append((diff, ni, nj))
            h_min = max(h_min, h)
            for diff, ni, nj in candidates:
                if diff <= h_min:
                    dfs(ni, nj, h_min)

        R, C = len(heights), len(heights[0])
        visited = [[0]*C for _ in range(R)]
        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        self.res = float('inf')
        dfs(0, 0, 0)
        return self.res


import heapq
class Solution:
    def minimumEffortPath(self, heights) -> int:
        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        R, C = len(heights), len(heights[0])
        dp = [[float('inf')]*C for _ in range(R)]
        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        pq = [(0,0,0)]
        while pq:
            dist, i, j = heapq.heappop(pq)
            dp[i][j] = dist
            if i == R-1 and j == C-1:
                return dist
            for di,dj in dir4:
                # print(di,dj)
                ni,nj = i+di,j+dj
                if inRange(ni,nj):
                    diff = max(dist, abs(heights[i][j] - heights[ni][nj]))
                    if diff < dp[ni][nj]:
                        dp[ni][nj] = diff
                        heapq.heappush(pq, (diff,ni,nj))
        return -1



from collections import deque
class Solution:
    def minimumEffortPath(self, heights) -> int:
        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        def bfs(h):
            q = deque([(0,0)])
            visited[0][0] = 1
            while q:
                i,j = q.popleft()
                if i == R-1 and j == C-1:
                    return True
                for di,dj in dir4:
                    ni,nj = i+di,j+dj
                    if inRange(ni,nj) and visited[ni][nj] == 0 and abs(heights[ni][nj] - heights[i][j]) <= h:
                        visited[ni][nj] = 1
                        q.append((ni,nj))
            return False

        R, C = len(heights), len(heights[0])
        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        h_min, h_max = float('inf'), -float('inf')
        for i in range(R):
            for j in range(C):
                h_min = min(h_min, heights[i][j])
                h_max = max(h_max, heights[i][j])
        left, right = 0, h_max - h_min
        while left < right:
            mid = (left + right)//2
            visited = [[0]*C for _ in range(R)]
            if bfs(mid):
                right = mid
            else:
                left = mid+1
        return left

S = Solution_2()
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(S.minimumEffortPath(heights))
heights = [[1,2,3],[3,8,4],[5,3,5]]
print(S.minimumEffortPath(heights))
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(S.minimumEffortPath(heights))