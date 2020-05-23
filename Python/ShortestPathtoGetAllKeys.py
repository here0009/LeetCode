"""
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

 

Example 1:

Input: ["@.a.#","###.#","b.A.B"]
Output: 8
Example 2:

Input: ["@..aA","..B#.","....b"]
Output: 6
 

Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
"""

class Solution_1:
    def shortestPathAllKeys(self, grid) -> int:
        """
        can travel back, use visited to store keys, if keys were larger than befor, then can visit if again
        try to use BFS
        """
        def inRange(x,y):
            return 0<=x<m and 0<=y<n

        def dfs(x,y,curr_keys,moves):
            print(x,y,curr_keys,moves,self.res)
            visited.add((x,y,curr_keys))
            if moves >= self.res:
                return
            g = grid[x][y]
            if g.islower() and g not in curr_keys:
                curr_keys += g
                curr_keys = ''.join(sorted(curr_keys))
            # print(g,curr_keys,moves)
            if len(curr_keys) == len_keys:
                self.res = min(self.res, moves)
                return
            elif (g.isupper() and g.lower() not in curr_keys) or g == '#':
                return
            for dx,dy in directions:
                if inRange(x+dx,y+dy) and  (x+dx,y+dy, curr_keys) not in visited:
                    dfs(x+dx, y+dy,curr_keys, moves+1)


        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        m,n = len(grid), len(grid[0])
        for row in grid:
            print(row)
        keys_set = set()
        # visitied = [[0]*n for _ in range(m)]
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    keys_set.add(grid[i][j])
                if grid[i][j] == '@':
                    start_x,start_y = i,j
        len_keys = len(keys_set)
        self.res = float('inf')
        # print(visitied)
        dfs(start_x, start_y, '', 0)
        # print(res)
        if self.res == float('inf'):
            return -1
        else:
            return self.res

import heapq
class Solution:
    def shortestPathAllKeys(self, grid) -> int:
        """
        can travel back, use visited to store keys, if keys were larger than befor, then can visit if again
        try to use BFS
        visited should not add moves, stupid!!!
        """
        def inRange(x,y):
            return 0<=x<m and 0<=y<n

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        m,n = len(grid), len(grid[0])
        # for row in grid:
        #     print(row)
        keys_set = set()


        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    keys_set.add(grid[i][j])
                if grid[i][j] == '@':
                    start_x,start_y = i,j
        
        len_keys = len(keys_set)
        self.res = float('inf')

        visited = set()
        bfs = [(0, start_x, start_y, '')]

        while bfs:
            moves,x,y,curr_keys= heapq.heappop(bfs)
            # print(x,y,curr_keys,grid[x][y])
            # print(bfs)
            visited.add((x,y,curr_keys))
            g = grid[x][y]
            if g.islower() and g not in curr_keys:
                curr_keys += g
                curr_keys = ''.join(sorted(curr_keys))
            if len(curr_keys) == len_keys:
                return moves
            elif (g.isupper() and (g.lower() not in curr_keys)) or g == '#':
                continue
            for dx,dy in directions:
                if inRange(x+dx,y+dy) and  (x+dx,y+dy,curr_keys) not in visited:
                    heapq.heappush(bfs,(moves+1,x+dx, y+dy,curr_keys))

        return -1

from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid) -> int:
        """
        can travel back, use visited to store keys, if keys were larger than befor, then can visit if again
        try to use BFS
        """
        def inRange(x,y):
            return 0<=x<m and 0<=y<n

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        m,n = len(grid), len(grid[0])
        keys_set = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    keys_set.add(grid[i][j])
                if grid[i][j] == '@':
                    start_x,start_y = i,j
        
        len_keys = len(keys_set)
        visited = set()
        bfs = deque([(0, start_x, start_y, '')])
        visited.add((start_x, start_y, ''))

        while bfs:
            moves,x,y,curr_keys= bfs.popleft()
            
            g = grid[x][y]
            if g.islower() and g not in curr_keys:
                curr_keys += g
                curr_keys = ''.join(sorted(curr_keys))
            if len(curr_keys) == len_keys:
                return moves
            elif (g.isupper() and (g.lower() not in curr_keys)) or g == '#':
                continue
            for dx,dy in directions:
                if inRange(x+dx,y+dy) and  (x+dx,y+dy,curr_keys) not in visited:
                    visited.add((x+dx, y+dy,curr_keys))
                    bfs.append((moves+1,x+dx, y+dy,curr_keys))

        return -1


class Solution_2:
    def shortestPathAllKeys(self, grid) -> int:
        """
        can travel back, use visited to store keys, if keys were larger than befor, then can visit if again
        try to use BFS
        this one can pass
        """
        def inRange(x,y):
            return 0<=x<m and 0<=y<n

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        m,n = len(grid), len(grid[0])
        keys_set = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    keys_set.add(grid[i][j])
                if grid[i][j] == '@':
                    start_x,start_y = i,j
        
        len_keys = len(keys_set)
        self.res = float('inf')

        visited = set()
        bfs = [(start_x, start_y, '')]
        visited.add((start_x, start_y, ''))
        moves = 0
        while bfs:
            bfs2 = []
            for x,y,curr_keys in bfs:
                g = grid[x][y]
                if g.islower() and g not in curr_keys:
                    curr_keys += g
                    curr_keys = ''.join(sorted(curr_keys))
                if len(curr_keys) == len_keys:
                    return moves
                elif (g.isupper() and (g.lower() not in curr_keys)) or g == '#':
                    continue
                for dx,dy in directions:
                    if inRange(x+dx,y+dy) and  (x+dx,y+dy,curr_keys) not in visited:
                        visited.add((x+dx, y+dy,curr_keys))
                        bfs2.append((x+dx, y+dy,curr_keys))

            bfs = bfs2
            moves += 1
        return -1



s = Solution()
grid = ["@.a.#","###.#","b.A.B"]
print(s.shortestPathAllKeys(grid))

grid = ["@..aA","..B#.","....b"]
print(s.shortestPathAllKeys(grid))

grid = ["@Aa"]
print(s.shortestPathAllKeys(grid))

grid = ["@...a",".###A","b.BCc"]
print(s.shortestPathAllKeys(grid))

grid = [".#.b.","A.#aB","#d...","@.cC.","D...#"]
# for row in grid:
#     print(row)
print(s.shortestPathAllKeys(grid))

grid = [".#........","......#..#",".#B#.#..#.","##...D.#..",".#.......#","##.....a..","...C.#...#","A...#.e.E#","c.@..#...d","#..#.#.b.#"]
for row in grid:
    print(row)
print(s.shortestPathAllKeys(grid))

grid = ["..Ff..#..e.#...",".....#.##...#..","....#.#...#....","##.......##...#","...@#.##....#..","#........b.....","..#...#.....##.",".#....#E...#...","......A.#D.#...","...#...#..#....","...a.#B#.......",".......c.....#.","....#...C#...#.","##.#.....d..#..",".#..#......#..."]
for row in grid:
    print(row)
print(s.shortestPathAllKeys(grid))