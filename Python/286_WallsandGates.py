"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/walls-and-gates
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        INF = (1<<31)-1
        if not rooms:
            return
        R, C = len(rooms), len(rooms[0])
        visited = [[0]*C for _ in range(R)]
        bfs = []
        for i in range(R):
            for j in range(C):
                if rooms[i][j] == 0:
                    bfs.append((i,j))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        distance = 1
        while bfs:
            bfs2 = []
            for i,j in bfs:
                for di,dj in directions:
                    ni,nj = i+di,j+dj
                    if inRange(ni,nj) and visited[ni][nj] == 0 and rooms[ni][nj] == INF:
                        visited[ni][nj] = 1
                        bfs2.append((ni,nj))
                        rooms[ni][nj] = distance
            bfs = bfs2
            distance += 1


S = Solution()
print(S.wallsAndGates(rooms))
