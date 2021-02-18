"""
A game is played by a cat and a mouse named Cat and Mouse.

The environment is represented by a grid of size rows x cols, where each element is a wall, floor, player (Cat, Mouse), or food.

Players are represented by the characters 'C'(Cat),'M'(Mouse).
Floors are represented by the character '.' and can be walked on.
Walls are represented by the character '#' and cannot be walked on.
Food is represented by the character 'F' and can be walked on.
There is only one of each character 'C', 'M', and 'F' in grid.
Mouse and Cat play according to the following rules:

Mouse moves first, then they take turns to move.
During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). They cannot jump over the wall nor outside of the grid.
catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a time, respectively. Cat and Mouse can jump less than the maximum length.
Staying in the same position is allowed.
Mouse can jump over Cat.
The game can end in 4 ways:

If Cat occupies the same position as Mouse, Cat wins.
If Cat reaches the food first, Cat wins.
If Mouse reaches the food first, Mouse wins.
If Mouse cannot get to the food within 1000 turns, Cat wins.
Given a rows x cols matrix grid and two integers catJump and mouseJump, return true if Mouse can win the game if both Cat and Mouse play optimally, otherwise return false.

 

Example 1:



Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
Output: true
Explanation: Cat cannot catch Mouse on its turn nor can it get the food before Mouse.
Example 2:



Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
Output: true
Example 3:

Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
Output: false
Example 4:

Input: grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
Output: false
Example 5:

Input: grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1
Output: true
 

Constraints:

rows == grid.length
cols = grid[i].length
1 <= rows, cols <= 8
grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.
There is only one of each character 'C', 'M', and 'F' in grid.
1 <= catJump, mouseJump <= 8
"""


from typing import List
from functools import lru_cache
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        def neighbors(idx, jump_len):
            i, j = divmod(idx, C)
            res = [idx]
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for j_len in range(jump_len + 1):
                    ni, nj = i + di * j_len, j + dj * j_len
                    if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != '#': # can not jump through the wall
                        res.append(ni * C + nj)
                    else:
                        break
            return res

        @lru_cache(None)
        def jump(m_pos, c_pos, turn):
            if c_pos == food or c_pos == m_pos or turn >= R * C * 2:
                return False
            if m_pos == food:
                return True
            if turn % 2 == 1:  # mouse
                for m2 in neighbors(m_pos, mouseJump):
                    if jump(m2, c_pos, turn + 1):
                        return True
                return False
            else:  # cat
                for c2 in neighbors(c_pos, catJump):
                    if not jump(m_pos, c2, turn + 1):
                        return False
                return True

        R, C = len(grid), len(grid[0])
        mouse, cat, food = [None] * 3

        walls = set()
        for i in range(R):
            for j in range(C):
                idx = i * C + j
                if grid[i][j] == 'M':
                    mouse = idx
                elif grid[i][j] == 'C':
                    cat = idx
                elif grid[i][j] == 'F':
                    food = idx
                elif grid[i][j] == '#':
                    walls.add(idx)

        return jump(mouse, cat, 1)


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0]) # dimensions 
        walls = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "F": food = (i, j)
                elif grid[i][j] == "C": cat = (i, j)
                elif grid[i][j] == "M": mouse = (i, j)
                elif grid[i][j] == "#": walls.add((i, j))
                    
        @lru_cache(None)
        def fn(cat, mouse, turn): 
            """Return True if mouse wins."""
            if cat == food or cat == mouse or turn >= m*n*2: return False 
            if mouse == food: return True  # mouse reaching food
            
            if not turn & 1: # mouse moving 
                x, y = mouse
                for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1): 
                    for jump in range(0, mouseJump+1):
                        xx, yy = x+jump*dx, y+jump*dy
                        if not (0 <= xx < m and 0 <= yy < n) or (xx, yy) in walls: break 
                        if fn(cat, (xx, yy), turn+1): return True 
                return False 
            else: # cat moving
                x, y = cat
                for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1): 
                    for jump in range(0, catJump+1):
                        xx, yy = x+jump*dx, y+jump*dy
                        if not (0 <= xx < m and 0 <= yy < n) or (xx, yy) in walls: break 
                        if not fn((xx, yy), mouse, turn+1): return False
                return True
                    
        return fn(cat, mouse, 0)


from typing import List
from functools import lru_cache
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        def neighbors(idx, jump_len):
            yield idx
            i, j = divmod(idx, C)
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for j_len in range(1, jump_len + 1):
                    ni, nj = i + di * j_len, j + dj * j_len
                    if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != '#': # can not jump through the wall
                        yield ni * C + nj
                    else:
                        break

        @lru_cache(None)
        def jump(m_pos, c_pos, turn):
            if c_pos == food or c_pos == m_pos or turn >= R * C * 2:
                return False
            if m_pos == food:
                return True
            if turn % 2 == 1:  # mouse
                for m2 in neighbors(m_pos, mouseJump):
                    if jump(m2, c_pos, turn + 1):
                        return True
                return False
            else:  # cat
                for c2 in neighbors(c_pos, catJump):
                    if not jump(m_pos, c2, turn + 1):
                        return False
                return True

        R, C = len(grid), len(grid[0])
        mouse, cat, food = [None] * 3

        walls = set()
        for i in range(R):
            for j in range(C):
                idx = i * C + j
                if grid[i][j] == 'M':
                    mouse = idx
                elif grid[i][j] == 'C':
                    cat = idx
                elif grid[i][j] == 'F':
                    food = idx
                elif grid[i][j] == '#':
                    walls.add(idx)

        return jump(mouse, cat, 1)

# https://leetcode.com/problems/cat-and-mouse-ii/discuss/1020763/Python3-BFS-Coloring-method-O(m2*n2*(m%2Bn))-regardless-of-max-steps-with-comments
import collections
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        # 0: draw; 1: mouse win; 2: cat win
        R, C = len(grid), len(grid[0])
        N = R * C
        # we will need to maintain 2 * i * j states, marking the result when at position (i,j)
        # and [mouseMove, catMove], who is going to win.
        # i, j are calculated as r * n + c
        dp = [[[0] * 2 for i in range(N)] for j in range(N)] 
        # dp[i][j]: mouse at i and cat at j.
        # dp[i][j][0]: mouse move; dp[i][j][1]: cat move
        queue1 = collections.deque() # mouse win
        queue2 = collections.deque() # cat win
        wall = set()
        food = -1
        cat = -1
        mouse = -1
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'M':
                    mouse = i * C + j
                elif grid[i][j] == 'C':
                    cat = i * C + j
                elif grid[i][j] == 'F':
                    food = i * C + j
                elif grid[i][j] == '#':
                    wall.add(i * C + j)
        # initial status
        for i in range(N):
            if i not in wall:
                dp[i][i][0] = dp[i][i][1] = 2 # cat catch mouse
                dp[food][i][0] = 1 # mouse get food
                dp[food][i][1] = 1 # mouse get food
                dp[i][food][0] = 2 # cat get food
                dp[i][food][1] = 2 # cat get food

                queue1.append((food,i,0))
                queue1.append((food,i,1))
                queue2.append((i, food, 0))
                queue2.append((i, food, 1))
                queue2.append((i,i,0))
                queue2.append((i,i,1))
                
        graph_cat = collections.defaultdict(set)
        graph_mouse = collections.defaultdict(set)
        for r in range(R):
            for c in range(C):
                if grid[r][c] != '#':
                    pos = r * C + c
                    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        for step in range(mouseJump + 1):
                            nr, nc = r + dr * step, c + dc * step
                            if not (0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#'):
                                break
                            graph_mouse[pos].add(nr * C + nc)
                    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        for step in range(catJump + 1):
                            nr, nc = r + dr * step, c + dc * step
                            if not (0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#'):
                                break
                            graph_cat[pos].add(nr * C + nc)
        
        # coloring
        while queue1:
            i, j, k = queue1.popleft()
            if k == 1: # last time mouse move
                for m in graph_mouse[i]:
                    if j != food and m != food and j != m and dp[m][j][0] <= 0: # we don't want to overwrite dp[i][i] cases
                        dp[m][j][0] = 1
                        queue1.append((m, j, 0))
            else:
                for n in graph_cat[j]:
                    if n != food and i != food and i != n and dp[i][n][1] <= 0:
                        dp[i][n][1] -= 1
                        if -dp[i][n][1] == len(graph_cat[n]):
                            dp[i][n][1] = 1 # cat has no better way, mouse win
                            queue1.append((i,n,1))
                            
        while queue2:
            i, j, k = queue2.popleft()
            if k == 0: # last time cat move
                for n in graph_cat[j]:
                    if n != food and i != food and i != n and dp[i][n][1] <= 0:
                        dp[i][n][1] = 2
                        queue2.append((i, n, 1))
            else:
                for m in graph_mouse[i]:
                    if j != food and m != food and j != m and dp[m][j][0] <= 0:
                        dp[m][j][0] -= 1
                        if -dp[m][j][0] == len(graph_mouse[m]):
                            dp[m][j][0] = 2
                            queue1.append((m, j, 0))
        
        for i in range(N):
            for j in range(N):
                for k in range(2):
                    if dp[i][j][k] < 0:
                        dp[i][j][k] = 0
        
        return dp[mouse][cat][0] == 1

S = Solution()
# grid = ["####F","#C...","M...."]
# catJump = 1
# mouseJump = 2
# print(S.canMouseWin(grid, catJump, mouseJump))

# grid = ["M.C...F"]
# catJump = 1
# mouseJump = 4
# print(S.canMouseWin(grid, catJump, mouseJump))

# grid = ["M.C...F"]
# catJump = 1
# mouseJump = 3
# print(S.canMouseWin(grid, catJump, mouseJump))

# grid = ["C...#","...#F","....#","M...."]
# catJump = 2
# mouseJump = 5
# print(S.canMouseWin(grid, catJump, mouseJump))

# grid = [".M...","..#..","#..#.","C#.#.","...#F"]
# catJump = 3
# mouseJump = 1

# print(S.canMouseWin(grid, catJump, mouseJump))

grid = ["........","F...#C.M","........"]
catJump = 2
mouseJump = 3
print(S.canMouseWin(grid, catJump, mouseJump))
