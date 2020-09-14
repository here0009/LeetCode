"""
A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as a 2-D array of cells, where 0 represents uninfected cells, and 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region -- the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night. There will never be a tie.

Can you save the day? If so, what is the number of walls required? If not, and the world becomes fully infected, return the number of walls used.

Example 1:
Input: grid = 
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
Output: 10
Explanation:
There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

[[0,1,0,0,0,0,1,1],
 [0,1,0,0,0,0,1,1],
 [0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,1]]

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
Example 2:
Input: grid = 
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.
Example 3:
Input: grid = 
[[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.
Note:
The number of rows and columns of grid will each be in the range [1, 50].
Each grid[i][j] will be either 0 or 1.
Throughout the described process, there is always a contiguous viral region that will infect strictly more uncontaminated squares in the next round.
"""
class Solution(object):
    """
    思路：BFS
        1. 获取感染区、扩散区和墙数：获取感染区中所有点、及每个区域的扩散点、墙数
        2. 建墙：选取扩散点数最多的区域，统计墙数，建墙后墙内节点设置为安全区
        3. 扩散：其他区域的扩散点设为感染区
        4. 重复以上过程，直至没有感染区
    """
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        
        def adj(i,j):
            for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= ii < m and 0 <= jj< n:
                    yield ii,jj
        
        def get_virus_areas(grid):
            areas = []
            dangers = []
            walls = []
            color = [[0] * n for i in range(m)]
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and color[i][j] == 0:
                        area = [(i,j)]
                        danger = set()
                        wall = 0
                        Q = [(i,j)]
                        color[i][j] = 1
                        while Q:
                            s,t = Q.pop(0)
                            for ii,jj in adj(s,t):
                                if grid[ii][jj] == 1 and color[ii][jj] == 0:
                                    color[ii][jj] = 1
                                    Q.append((ii,jj))
                                    area.append((ii,jj))
                                if grid[ii][jj] == 0:
                                    wall += 1
                                    danger.add((ii,jj))
                        areas.append(area)
                        dangers.append(danger)
                        walls.append(wall)
            return areas,dangers,walls
        
        def spread(dangers):
            for danger in dangers:
                for i,j in danger:
                    grid[i][j] = 1
        
        wall_count = 0
        areas,dangers,walls = get_virus_areas(grid)
        while areas:
            print("++++++")
            for row in grid:
                print(row)
            # 如果全是感染区，返回
            n_area = len(areas)
            if sum(len(area) for area in areas) == m * n:
                return wall_count
            
            # 获取危险点最多的区域
            dangerest_i = 0
            for i in range(n_area):
                if len(dangers[i]) > len(dangers[dangerest_i]):
                    dangerest_i = i
            
            # 建墙，统计墙数，将对应感染区变为安全区
            wall_count += walls[dangerest_i]
            for i,j in areas[dangerest_i]:
                grid[i][j] = -1
            
            # 其他感染区扩散
            print(areas, 'len_area', len(areas), dangers, dangerest_i, list(map(len, dangers)), len(dangers))
            spread(dangers[:dangerest_i] + dangers[dangerest_i+1:])
            
            # 重新获取感染区
            areas,dangers,walls = get_virus_areas(grid)
        
        return wall_count

class Solution:
    def containVirus(self, grid) -> int:
        """
        the cells in danger is not equal to the walls need to built, some time you neeed to build 4 walls to protect a cell, e.g.
        111
        101
        111
        the walls neeed to build equalt to the 1s that got 0 as its neighbor
        """
        

        def neighbor(i, j):
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                if 0 <= i+di < R and 0 <= j+dj < C:
                    yield i+di, j+dj

        def getArea(grid):
            visited = [[0]*C for _ in range(R)]
            areas_list = []
            indangers_list = []
            walls_list = []
            for i in range(R):
                for j in range(C):
                    if grid[i][j] == 1 and visited[i][j] == 0:
                        area = [(i,j)]
                        indanger = set()
                        wall = 0
                        bfs = [(i,j)]
                        visited[i][j] = 1
                        while bfs:
                            bfs2 = []
                            # for i,j in bfs: #a very bad mistake, change i,j during the iteration.
                            #     for ni,nj in neighbor(i,j):
                            for p,q in bfs:
                                for ni, nj in neighbor(p,q):
                                    if grid[ni][nj] == 1 and visited[ni][nj] == 0:
                                        visited[ni][nj] = 1
                                        bfs2.append((ni,nj))
                                        area.append((ni,nj))
                                    elif grid[ni][nj] == 0:
                                        wall += 1
                                        indanger.add((ni,nj))
                            bfs = bfs2

                        areas_list.append(area)
                        indangers_list.append(indanger)
                        walls_list.append(wall)
            return areas_list, indangers_list, walls_list

        def spread(lst):
            for danger in lst:
                for i,j in danger:
                    grid[i][j] = 1

        res = 0
        R, C = len(grid), len(grid[0])
        areas_list, indangers_list, walls_list = getArea(grid)
        while areas_list:
            # print("++++++")
            # for row in grid:
            #     print(row)
            n_area = len(areas_list)
            # if sum(len(area) for area in areas_list) == R*C:
            #     return res
            most_danger_index = 0
            for i in range(n_area):
                if len(indangers_list[i]) > len(indangers_list[most_danger_index]):
                    most_danger_index = i

            res += walls_list[most_danger_index]
            for i,j in areas_list[most_danger_index]:
                grid[i][j] = -1 #already controled, no spread next round
            # print(areas_list, 'len_area', len(areas_list), indangers_list, most_danger_index, list(map(len, indangers_list)), len(indangers_list))
            spread(indangers_list[:most_danger_index] + indangers_list[most_danger_index+1:])
            areas_list, indangers_list, walls_list = getArea(grid)
        return res

S = Solution()
# grid = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
# print(S.containVirus(grid))
# grid = [[1,1,1],[1,0,1],[1,1,1]]
# print(S.containVirus(grid))
# grid = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
# print(S.containVirus(grid))
grid = [[1,0,0,1,0,1,1,0,0,0],[1,1,0,0,1,0,0,0,1,0],[0,1,1,0,1,0,0,0,1,0],[1,0,0,1,1,1,1,0,0,0],[0,0,1,1,1,0,0,0,1,0],[1,0,1,1,0,0,0,1,1,0],[1,0,0,0,1,0,1,1,1,0],[1,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0,0,0],[1,0,0,0,0,0,1,0,0,0]]
print(S.containVirus(grid))
# Output
# 59
# Expected
# 65