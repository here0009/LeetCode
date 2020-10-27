"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-distinct-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numDistinctIslands(self, grid) -> int:
        """
        Thoughts; use bit mask to represent the row of island
        """
        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        def dfs(i, j, res):
            visited[i][j] = 1
            res.append((i,j))
            for di, dj in dir4:
                ni, nj = i+di, j+dj
                if inRange(ni, nj) and visited[ni][nj] == 0 and grid[ni][nj] == 1:
                    dfs(ni, nj, res)

        def island_tuple(lst):
            """
            change list of nodes to string
            """
            lst = sorted(lst)
            min_i, min_j = R, C
            for i, j in lst:
                min_i, min_j = min(min_i, i), min(min_j, j)
            return tuple([(i-min_i)*C + (j-min_j) for i,j in lst])

        R, C = len(grid), len(grid[0])
        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        islands = set()
        visited = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    lst = []
                    dfs(i,j,lst)
                    # print(lst)
                    islands.add(island_tuple(lst))
        # print(islands)
        return len(islands)


# 作者：luoyh15
# 链接：https://leetcode-cn.com/problems/number-of-distinct-islands/solution/dfsji-he-qu-zhong-by-luoyh15/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def numDistinctIslands(self, grid) -> int:
        def inRange(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i, j, stack):
            grid[i][j] = 2
            oi, oj = stack[0]
            stack.append((i-oi, j-oj))
            for di,dj in dir4:
                ni, nj = i+di, j+dj
                if inRange(ni, nj) and grid[ni][nj] == 1:
                    dfs(ni, nj, stack)

        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(grid), len(grid[0])
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = [(i,j)]
                    dfs(i, j, stack)
                    islands.add(tuple(stack[1:]))
        return len(islands)


S = Solution()
# grid = ["11000","11000","00011","00011",]
# print(S.numDistinctIslands(grid))
# grid = ["11011","10000","00001","11011"]
# print(S.numDistinctIslands(grid))
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(S.numDistinctIslands(grid))