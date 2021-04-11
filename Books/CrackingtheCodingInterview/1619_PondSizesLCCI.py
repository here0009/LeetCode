"""
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

示例：

输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]
提示：

0 < len(land) <= 1000
0 < len(land[i]) <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pond-sizes-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:

        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        def neighbors(i, j):
            for di, dj in dir8:
                ni, nj = i + di, j + dj
                if inRange(ni, nj) and visited[ni][nj] == 0 and land[ni][nj] == 0:
                    yield ni, nj

        def dfs(i, j):
            # print(i, j)
            res = 1
            visited[i][j] = 1
            for ni, nj in neighbors(i, j):
                res += dfs(ni, nj)
            return res

        R, C = len(land), len(land[0])
        dir8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        visited = [[0] * C for _ in range(R)]
        res = []
        # for row in land:
        #     print(row)
        for i in range(R):
            for j in range(C):
                if visited[i][j] == 0 and land[i][j] == 0:
                    res.append(dfs(i, j))
        return sorted(res)

S = Solution()
land = [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]
print(S.pondSizes(land))
