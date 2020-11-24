"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

|x| + |y| <= 300
"""
class Solution_1:
    def minKnightMoves(self, x, y):
        x2,x1 = divmod(x,2)
        y2,y1 = divmod(y,2)
        print(x2,x1)
        print(y2,y1)
        return max(x2,y1) + max(x1,y2)


class Solution:
    def minKnightMoves(self, x, y):
        if x < y:
            x,y = y,x
        if x //y >= 2:
            return x//2
        else:
            x2,x1 = divmod(x,2)
            y2,y1 = divmod(y,2)
            return max(x2,y1) + max(x1,y2)


class Solution:
    def minKnightMoves(self, x, y):
        if x < y:
            x,y = y,x
        counts = 0
        while x != 0 or y != 0:
            print(x,y)
            if x - y == 3:
                x += 1
                y += 2
            else:
                if abs(x) >= 2*abs(y):
                    if x > 0:
                        x -= 2
                    else:
                        x += 2
                    if y > 0:
                        y -= 1
                    else:
                        y += 1
                else:
                    if x > 0:
                        x -= 1
                    else:
                        x += 1
                    if y > 0:
                        y -= 2
                    else:
                        y += 2
            counts += 1
        return counts


class Solution:
    def minKnightMoves(self, x, y):
        visited = set()
        visited.add((0,0))
        bfs = set()
        bfs.add((0,0))
        dir8 = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
        steps = 0
        if (x, y) == (0, 0):
            return 0
        steps = 1
        threshold = 100
        while bfs:
            bfs2 = set()
            for i, j in bfs:
                for di,dj in dir8:
                    ni, nj = i+di, j+dj
                    if (ni, nj) == (x, y):
                        return steps
                    if (ni, nj) not in visited:
                        if (-threshold + min(i, ni) <= x <= max(i, ni)+threshold) or (-threshold+min(j, nj) <= y <= max(j, nj)+threshold):
                            visited.add((ni, nj))
                            bfs2.add((ni, nj))
            bfs = bfs2
            steps += 1
        return None

# 4个象限对称，可以只考虑第一象限
class Solution:
    def minKnightMoves(self, x, y):
        if x == 0 and y == 0:
            return 0
        # 只关注第一象限
        x, y = abs(x), abs(y)
        visited = set()
        cur, nxt = [], []
        cur.append((0, 0))
        steps = 1
        while cur:
            for r, c in cur:
                for nr, nc in self.neighbour(r, c):
                    # 向(x, y)点附近扩散
                    if -2 < nr < x + 3 and -2 < nc < y + 3 and (nr, nc) not in visited:
                        if nr == x and nc == y:
                            return steps
                        visited.add((nr, nc))
                        nxt.append((nr, nc))
            cur, nxt = nxt, []
            steps += 1
        return -1
    
    def neighbour(self, r, c):
        offset = [-2, -1, 1, 2]
        return [(r + i, c + j) for i in offset for j in offset if abs(i) != abs(j)]         

s = Solution()
x = 2
y = 1
print(s.minKnightMoves(x,y))

x = 5
y = 5
print(s.minKnightMoves(x,y))

x = 2
y = 112
print(s.minKnightMoves(x,y))

x = 217
y = 47
print(s.minKnightMoves(x,y))
"""
Output:
108
Expected:
110
"""

x = 130
y = -86
print(s.minKnightMoves(x,y))
"""
Output:
92
Expected:
72
"""