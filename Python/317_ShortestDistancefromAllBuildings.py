"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-distance-from-all-buildings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
class Solution_1:
    def shortestDistance(self, grid) -> int:
        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        R, C = len(grid), len(grid[0])
        buildings = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    buildings.append((i,j))

        distance = defaultdict(list)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for p,q in buildings:
            bfs, d = [(p,q)], 1
            visited = set()
            while bfs:
                bfs2 = []
                for i,j in bfs:
                    for di,dj in directions:
                        ni,nj = i+di, j+dj
                        if inRange(ni,nj) and ((ni,nj) not in visited) and grid[ni][nj] == 0:
                            visited.add((ni,nj))
                            bfs2.append((ni,nj))
                            distance[(ni,nj)].append(d)
                bfs = bfs2
                d += 1

        res = float('inf')
        target = len(buildings)
        for lst in distance.values():
            if len(lst) == target:
                res = min(res, sum(lst))

        return res if res != float('inf') else -1



class Solution:
    def shortestDistance(self, grid) -> int:

        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        R, C = len(grid), len(grid[0])
        distance = [[0]*C for _ in range(R)]
        counts = [[0]*C for _ in range(R)] 
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        buildings = 0
        for p in range(R):
            for q in range(C):
                if grid[p][q] == 1:
                    buildings += 1
                    visited = [[0]*C for _ in range(R)]
                    bfs, d = [(p,q)], 1
                    while bfs:
                        bfs2 = []
                        for i,j in bfs:
                            for di,dj in directions:
                                ni,nj = i+di, j+dj
                                if inRange(ni,nj) and visited[ni][nj] == 0 and grid[ni][nj] == 0:
                                    distance[ni][nj] += d
                                    counts[ni][nj] += 1
                                    visited[ni][nj] = 1
                                    bfs2.append((ni,nj))
                        bfs = bfs2
                        d += 1
        
        res = float('inf')
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0 and counts[i][j] == buildings:
                    res = min(res, distance[i][j])

        return res if res != float('inf') else -1




# 作者：zql-sd
# 链接：https://leetcode-cn.com/problems/shortest-distance-from-all-buildings/solution/python-bfs-by-zql-sd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


S = Solution_1()
grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(S.shortestDistance(grid))
grid = [[0,2,0,0,2,2,2,2,2,2,2,0,0,0,0,2,2,1,0,0,2,0,2,0,2,0,0,2,2,2,0,0,2,0,2,0,2,2,2,0,2],[0,0,0,0,0,2,2,0,2,0,0,0,0,0,2,0,0,2,2,0,2,2,2,2,0,0,2,2,0,0,2,2,1,0,0,2,2,0,2,0,0],[0,0,0,0,2,2,0,0,0,0,0,0,2,2,0,2,2,0,0,0,2,2,2,2,0,0,0,0,2,2,0,0,0,0,0,2,0,0,2,2,0],[2,2,0,2,0,0,2,0,0,0,0,0,2,2,2,0,2,2,2,0,0,0,0,0,0,1,2,2,0,0,0,0,2,0,0,2,0,0,0,0,2],[0,0,2,2,0,0,2,1,2,0,0,0,0,2,1,0,2,2,0,2,0,0,0,2,1,0,2,2,0,0,0,2,0,0,0,2,2,0,2,0,0],[0,0,2,2,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,2,2,2,2,2,0,2,2,1,2,0,2,0,0,0,2,0,2,2,0],[2,0,0,0,2,2,0,0,0,2,1,0,2,0,0,0,0,2,0,2,0,2,2,2,0,2,2,2,0,0,0,0,0,0,2,0,0,0,0,0,2],[1,0,2,2,0,0,2,0,0,0,2,0,0,0,2,2,2,2,0,0,0,0,2,0,0,2,0,2,1,2,2,0,0,2,0,0,0,0,0,0,0],[0,2,0,0,0,1,0,0,2,2,0,0,0,0,2,0,0,2,0,2,2,2,0,0,2,2,0,2,2,2,2,0,0,0,0,2,0,2,0,0,2],[0,0,2,2,0,2,2,0,2,0,1,0,0,0,0,0,2,0,0,2,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,2,2,0,0,1],[1,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,2,0],[0,1,2,2,2,2,0,2,0,0,2,2,0,0,0,0,0,2,0,2,0,0,0,0,2,0,0,0,0,0,0,2,2,2,0,0,2,2,0,0,0],[2,0,2,0,2,0,0,2,0,0,0,2,0,0,2,2,0,0,0,2,0,0,2,2,2,0,2,2,0,2,2,1,2,0,0,2,0,0,0,2,0],[0,0,2,0,0,0,2,2,2,0,2,2,2,0,0,2,0,0,0,2,1,2,2,0,2,0,2,0,0,2,2,0,0,0,2,2,0,0,0,0,0],[0,0,0,0,0,2,2,0,2,0,0,2,0,2,0,0,0,2,0,0,0,0,0,0,0,1,2,0,0,0,0,1,0,2,0,0,2,0,1,0,0],[1,2,0,2,0,0,0,2,0,2,0,0,0,0,0,2,1,2,0,0,0,0,0,2,0,0,0,0,0,2,2,0,0,0,2,0,0,1,0,2,2],[1,0,0,2,0,2,0,2,0,2,0,0,0,0,1,0,0,0,0,0,2,2,0,2,0,2,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,1,2,2,0,0,2,2,0,0,0,0,0,0,2,0,2,0,2,2,0,1],[2,0,0,1,1,0,1,0,2,0,0,2,1,0,2,0,0,2,2,0,2,0,2,2,0,1,2,0,2,0,0,0,0,0,0,2,0,0,2,0,0],[2,2,0,0,0,2,2,0,2,2,0,0,0,2,0,0,0,2,0,0,2,0,0,2,0,0,0,2,0,0,0,2,2,2,0,2,0,0,2,0,2]]
print(S.shortestDistance(grid))