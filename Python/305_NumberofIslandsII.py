"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numIslands2(self, m: int, n: int, positions):
        """
        union-find
        """
        def find(p):
            if root[p] != p:
                root[p] = find(root[p])
            return root[p]

        def union(p, q):
            root_p = find(p)
            root_q = find(q)
            if root_p == root_q:
                return False
            else:
                root[root_q] = root_p
                return True

        root = dict()
        for i in range(m):
            for j in range(n):
                root[(i,j)] = (i,j)

        grid = [[0]*n for _ in range(m)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        nodes = 0
        res = []
        for i,j in positions:
            if grid[i][j] == 1:
                res.append(nodes)
                continue
            grid[i][j] = 1
            nodes += 1
            for di,dj in directions:
                ni,nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 1:
                        nodes -= union((i,j),(ni,nj))
            res.append(nodes)
        return res


S = Solution()
m = 3
n = 3
positions = [[0,0], [0,1], [1,2], [2,1]]
print(S.numIslands2(m, n, positions))

m = 3
n = 3
positions = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
print(S.numIslands2(m, n, positions))
# 输出：
# [1,2,3,4,3,2,-1]
# 预期结果：
# [1,2,3,4,3,2,1]