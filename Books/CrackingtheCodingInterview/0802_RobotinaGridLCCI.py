"""
设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。



网格中的障碍物和空位置分别用 1 和 0 来表示。

返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
解释: 
输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/robot-in-a-grid-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        def neighbors(i, j):
            for di, dj in dir2:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and obstacleGrid[ni][nj] == 0:
                    yield ni, nj

        def trackPath(pos):
            res = []
            while pos:
                res.append(list(pos))
                pos = visited[pos]
            return res[::-1]


        bfs = [(0, 0)]
        visited = dict()
        dir2 = [(0, 1), (1, 0)]
        # dir4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R = len(obstacleGrid)
        if R == 0:
            return []
        C = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return []
        # for row in obstacleGrid:
        #     print(row)
        target = (R - 1, C - 1)
        visited[(0, 0)] = None
        while bfs:
            bfs2 = []
            for i, j in bfs:
                if (i, j) == target:
                    return trackPath((i, j))
                for ni, nj in neighbors(i, j):
                    if (ni, nj) not in visited:
                        visited[(ni, nj)] = (i, j)
                        bfs2.append((ni, nj))
            bfs = bfs2
        return []

S = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(S.pathWithObstacles(obstacleGrid))

obstacleGrid = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[1,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]]
output = [[0,0],[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[9,1],[10,1],[11,1],[12,1],[13,1],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[18,1],[19,1],[20,1],[21,1],[21,0],[22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],[29,0],[30,0],[31,0],[32,0],[32,1],[33,1],[34,1],[35,1],[36,1],[37,1],[38,1],[39,1],[40,1]]
print(S.pathWithObstacles(obstacleGrid))
