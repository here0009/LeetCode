"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""
class Solution:
    def countServers(self, grid) -> int:
        def dfs(i,j):
            visited[i][j] = 1
            self.cluster_n += 1
            for di in range(1,m):
                dx = (i+di)%m
                if not visited[dx][j] and grid[dx][j] == 1:
                    dfs(dx,j)
            for dj in range(1,n):
                dy = (j+dj)%n
                if not visited[i][dy] and grid[i][dy] == 1:
                    dfs(i,dy)



        m,n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    self.cluster_n = 0
                    dfs(i,j)
                    if self.cluster_n > 1:
                        res += self.cluster_n
        return res

s = Solution()
grid = [[1,0],[0,1]]
print(s.countServers(grid))


grid = [[1,0],[1,1]]
print(s.countServers(grid))


grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
print(s.countServers(grid))


grid = [[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]
print(s.countServers(grid))