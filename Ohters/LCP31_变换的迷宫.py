"""
某解密游戏中，有一个 N*M 的迷宫，迷宫地形会随时间变化而改变，迷宫出口一直位于 (n-1,m-1) 位置。迷宫变化规律记录于 maze 中，maze[i] 表示 i 时刻迷宫的地形状态，"." 表示可通行空地，"#" 表示陷阱。

地形图初始状态记作 maze[0]，此时小力位于起点 (0,0)。此后每一时刻可选择往上、下、左、右其一方向走一步，或者停留在原地。

小力背包有以下两个魔法卷轴（卷轴使用一次后消失）：

临时消除术：将指定位置在下一个时刻变为空地；
永久消除术：将指定位置永久变为空地。
请判断在迷宫变化结束前（含最后时刻），小力能否在不经过任意陷阱的情况下到达迷宫出口呢？

注意： 输入数据保证起点和终点在所有时刻均为空地。

示例 1：

输入：maze = [[".#.","#.."],["...",".#."],[".##",".#."],["..#",".#."]]

输出：true

解释：
maze.gif

示例 2：

输入：maze = [[".#.","..."],["...","..."]]

输出：false

解释：由于时间不够，小力无法到达终点逃出迷宫。

示例 3：

输入：maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]

输出：false

解释：由于道路不通，小力无法到达终点逃出迷宫。

提示：

1 <= maze.length <= 100
1 <= maze[i].length, maze[i][j].length <= 50
maze[i][j] 仅包含 "."、"#"
"""

from typing import List
from functools import lru_cache
class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        """
        enumerate all the possible board
        """
        # for i, time in enumerate(maze):
        #     print(time, i)
        #     for row in time:
        #         print(row)

        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        def neighbors(p):
            i, j = p
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                ni, nj = i + di, j + dj
                if inRange(ni, nj):
                    yield tuple([ni, nj])

        @lru_cache(None)
        def dfs(p, a, b, mi):
            """
            a is temp, b is permernant idx
            """
            if p[0] == R - 1 and p[1] == C - 1:
                return True
            if mi == len_maze - 1:
                return False
            i, j = p
            if maze[mi][i][j] == '.' or (maze[mi][i][j] == '#' and b == p):
                return any([dfs(np, a, b, mi + 1) for np in neighbors(p)])
            if maze[mi][i][j] == '#':
                if a:
                    if any([dfs(np, False, b, mi + 1) for np in neighbors(p)]):
                        return True
                if b is None:
                    if any([dfs(np, a, p, mi + 1) for np in neighbors(p)]):
                        return True
            return False

        R, C = len(maze[0]), len(maze[0][0])
        len_maze = len(maze)

        return dfs((0, 0), True, None, 0)


from typing import List
from functools import lru_cache
class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        """
        enumerate all the possible board
        """

        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        def neighbors(p):
            i, j = p
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                ni, nj = i + di, j + dj
                if inRange(ni, nj):
                    yield tuple([ni, nj])

        @lru_cache(None)
        def dfs(p, a, b, mi):
            """
            a is temp, b is permernant status
            """
            if p[0] == R - 1 and p[1] == C - 1:
                return True
            if mi == len_maze - 1 or (R - 1 - p[0] + C - 1 - p[1] > len_maze - 1 - mi):
                return False
            # i, j = p
            for np in neighbors(p):
                if maze[mi][p[0]][p[1]] == '.' or (maze[mi][p[0]][p[1]] == '#' and b == p):
                    if dfs(np, a, b, mi + 1):
                        return True
                else:
                    if not a and b is not None:
                        continue
                    if a and dfs(np, False, b, mi + 1):
                        return True
                    if b is None:
                        if dfs(np, a, p, mi + 1):
                            return True
            return False

        len_maze, R, C = len(maze), len(maze[0]), len(maze[0][0])
        return dfs((0, 0), True, None, 0)


from typing import List
from functools import lru_cache
class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        """
        enumerate all the possible board
        """

        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        def neighbors(p):
            i, j = p
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                ni, nj = i + di, j + dj
                if inRange(ni, nj):
                    yield tuple([ni, nj])

        @lru_cache(None)
        def dfs(p, a, b, mi):
            """
            a is temp, b is permernant status
            """
            if p[0] == R - 1 and p[1] == C - 1:
                return True
            if mi == len_maze - 1 or (R - 1 - p[0] + C - 1 - p[1] > len_maze - 1 - mi):
                return False
            # i, j = p
            for np in neighbors(p):
                if maze[mi][p[0]][p[1]] == '.':
                    if dfs(np, a, b, mi + 1):
                        return True
                else:
                    if not a and not b:
                        continue
                    if a and dfs(np, False, b, mi + 1):
                        return True
                    if b:
                        for mi2 in range(mi + 1, len_maze):
                            if dfs(np, a, False, mi2):
                                return True
            return False

        len_maze, R, C = len(maze), len(maze[0]), len(maze[0][0])
        return dfs((0, 0), True, True, 0)

# 作者：iimmortall
# 链接：https://leetcode-cn.com/problems/Db3wC1/solution/yan-du-you-xian-sou-suo-by-iimmortall-qhk0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        Z = len(maze)
        Y = len(maze[0])
        X = len(maze[0][0])
        # 坐标x, 坐标y, 时间, 临时消除术次数, 永久消除术剩余次数
        stack = [(0, 0, 0, 1, 1)]
        visited = set()
        while stack:
            p = stack.pop()
            if p in visited:
                continue
            visited.add(p)
            x, y, z, roll1, roll2 = p
            if z == Z or x == -1 or x == X or y == -1 or y == Y:
                continue
            if Y-y-1 + X-x-1 > Z-z-1:
                continue
            if x == X-1 and y == Y-1:
                return True
            if maze[z][y][x] == '#':
                if roll1:
                    stack.append((x, y, z+1, 2, roll2))
                    stack.append((x-1, y, z+1, 0, roll2))
                    stack.append((x+1, y, z+1, 0, roll2))
                    stack.append((x, y-1, z+1, 0, roll2))
                    stack.append((x, y+1, z+1, 0, roll2))
                if roll2 and roll1 != 2:
                    stack.append((x-1, y, z+1, roll1, 0))
                    stack.append((x+1, y, z+1, roll1, 0))
                    stack.append((x, y-1, z+1, roll1, 0))
                    stack.append((x, y+1, z+1, roll1, 0))
                continue
            if roll1 == 2:
                stack.append((x, y, z+1, 2, roll2))
                stack.append((x-1, y, z+1, 0, roll2))
                stack.append((x+1, y, z+1, 0, roll2))
                stack.append((x, y-1, z+1, 0, roll2))
                stack.append((x, y+1, z+1, 0, roll2))
            else:
                stack.append((x, y, z+1, roll1, roll2))
                stack.append((x-1, y, z+1, roll1, roll2))
                stack.append((x+1, y, z+1, roll1, roll2))
                stack.append((x, y-1, z+1, roll1, roll2))
                stack.append((x, y+1, z+1, roll1, roll2))
        return False



# 作者：moguqicha
# 链接：https://leetcode-cn.com/problems/Db3wC1/solution/dfsbfstong-li-by-moguqicha-vb0k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        time = len(maze)
        X = len(maze[0])
        Y = len(maze[0][0])
        stk = []
        stk.append((0, 0, 0, 1, 1))  #  时刻、坐标x、坐标y、卷轴1、卷轴2
        seen = set()
        while stk:
            cur = stk.pop()
            if cur in seen:
                continue
            seen.add(cur)
            x, y, t, roll1, roll2 = cur
            if t == time:  # 时间花完，
                continue
            if Y-y-1 + X-x-1 > time-t-1:  # 走完剩下的路需要的最小时间 < 剩余时间，那么此路不通
                continue
            if x == X-1 and y == Y-1:
                return True
            if maze[t][x][y] == '#':# 使用一个卷轴
                if roll1: # 使用roll1
                    stk.append((x, y, t+1, 2, roll2)) # 原地不动
                    for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                        curx, cury = x + dx, y + dy
                        if 0 <= curx < X and 0 <= cury < Y:
                            stk.append((curx, cury, t+1, 0, roll2))
                if roll2 and roll1 != 2:# 使用卷轴2，如果使用卷轴1并且没有动，就不能使用卷轴2
                    for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                        curx, cury = x + dx, y + dy
                        if 0 <= curx < X and 0 <= cury < Y:
                            stk.append((curx, cury, t+1, roll1, 0))
                continue
            if roll1 == 2:
                stk.append((x, y, t+1, 2, roll2)) # 原地不动
                for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                    curx, cury = x + dx, y + dy
                    if 0 <= curx < X and 0 <= cury < Y:
                        stk.append((curx, cury, t+1, 0, roll2))
            else:
                stk.append((x, y, t+1, roll1, roll2)) # 原地不动
                for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                    curx, cury = x + dx, y + dy
                    if 0 <= curx < X and 0 <= cury < Y:
                        stk.append((curx, cury, t+1, roll1, roll2))
        return False



S = Solution()
maze = [[".#.","#.."],["...",".#."],[".##",".#."],["..#",".#."]]
print(S.escapeMaze(maze))
maze = [[".#.","..."],["...","..."]]
print(S.escapeMaze(maze))
maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]
print(S.escapeMaze(maze))
maze = [["...",".##","##.","#.#",".##","...",".#.","##.","##."],[".##","###","##.",".##",".##","##.",".#.","###","##."],[".##","###","###",".##","##.","##.","#.#","###",".#."],[".##","#.#",".##","#.#","###","#.#","###","...",".#."],["..#","###","#..",".##",".##","..#",".#.","###",".#."],["..#",".#.","..#",".##","###","#.#","#..","###","##."],[".##","..#",".##",".#.","##.","###","##.","###","##."],[".##","..#","#.#",".##","###",".##","##.",".##","#.."],["...","##.","#.#","..#","##.","..#",".##","#.#","##."],[".##","###","###","#.#",".##",".##","###","###","#.."],["..#","###","..#","#..",".#.","###","#.#","###",".#."],["..#","###","##.","##.",".#.","#..","###","##.",".#."],[".##","#.#",".#.",".##",".#.","###",".#.","###","##."],[".#.","#.#",".##","#..","#.#","##.","###","###","##."],["..#","###","###","###","##.",".#.","##.","###","##."],["..#","#..",".#.","##.","###","...",".##","#.#",".#."],[".##","###",".##",".##","###","#..","###","...",".#."],[".##",".##","##.","#..","###","..#","...","###","##."],[".##","#..","###","###","##.","#..",".##","..#","##."],["...",".#.","###","###","###","###","##.","#.#",".#."],[".##",".#.","#..","#.#","###","##.",".#.","###",".#."],["..#","###","###","###","#.#","##.","##.","#.#","#.."],["...","###","###","##.","#.#",".#.","#.#","#..",".#."],[".##","..#","##.",".##","###","#..","#.#","#.#","##."],["..#","###","###","##.",".##",".##","#.#","#..",".#."],["..#","..#","#..","...",".##","##.","#.#","##.","##."],[".#.","##.","#.#","##.","#.#","##.","###",".#.","##."],[".#.","###","..#","###",".##","..#",".#.","###","##."],[".#.","###","###","##.","###",".##","##.","##.",".#."],[".#.",".##","###",".#.",".#.",".#.","###","###","..."],[".##","#.#",".##","###","###",".##",".##",".##","##."],["..#","##.",".#.",".##","###","###","###",".##","##."],[".#.",".##","##.","#..","###",".#.",".#.","#.#","##."],[".#.","###","...","###","##.",".#.","#.#",".##","##."],["..#","#..","#.#",".##","###","##.",".#.","##.","##."],["..#","##.","###","###","#..","##.","##.",".##","##."],["..#","###",".##","..#",".#.",".##",".##","###",".#."],["..#",".#.",".##",".#.",".#.",".##","#.#","##.","##."],["..#","###","#..","...","#..",".##","..#",".##","..."],[".##","###","#..","###","#.#","##.","#..","###","##."]]
print(S.escapeMaze(maze))