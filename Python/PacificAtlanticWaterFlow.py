"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, bottom, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
class Solution_1:
    def pacificAtlantic(self, matrix):
        res = []
        row = len(matrix)
        col = len(matrix[0])
        leftUpMax = [[0]*(col + 1) for _ in range(row + 1)]
        rightBottomMax = [[0]*(col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                leftUpMax[i][j] = max(min(leftUpMax[i-1][j], leftUpMax[i][j-1]),matrix[i-1][j-1])

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                rightBottomMax[i][j] = max(min(rightBottomMax[i+1][j], rightBottomMax[i][j+1]), matrix[i][j])

                if matrix[i][j] >= leftUpMax[i+1][j+1] and matrix[i][j] >= rightBottomMax[i][j]:
                    res.append([i,j])
        for row in leftUpMax:
            print(row)
        print("+++++++++")
        for row in rightBottomMax:
            print(row)
        return res


class Solution_2:
    def pacificAtlantic(self, matrix):
        """
        wrong answer
        """
        res = []
        row = len(matrix)
        col = len(matrix[0])
        leftM = [[0]*col for _ in range(row)]
        upM = [[0]*col for _ in range(row)]
        rightM = [[0]*col for _ in range(row)]
        bottomM = [[0]*col for _ in range(row)]
        for i in range(row):
            leftMax = float('-inf')
            for j in range(col):
                leftMax = max(leftMax, matrix[i][j])
                leftM[i][j] = leftMax
            rightMax = float('-inf')
            for j in range(col-1, -1, -1):
                rightMax = max(rightMax, matrix[i][j])
                rightM[i][j] = rightMax

        for j in range(col):
            uPMax = float('-inf')
            for i in range(row):
                uPMax = max(uPMax, matrix[i][j])
                upM[i][j] = uPMax
            bottomMax = float('-inf')
            for i in range(row - 1, -1, -1):
                bottomMax = max(bottomMax, matrix[i][j])
                bottomM[i][j] = bottomMax

        for i in range(row):
            for j in range(col):
                if matrix[i][j] >= min(leftM[i][j], upM[i][j]) and matrix[i][j] >= min(rightM[i][j], bottomM[i][j]):
                    res.append([i,j])

        print("left==================")
        for row in leftM:
            print(row)
        print("up==================")
        for row in upM:
            print(row)
        print("right==================")
        for row in rightM:
            print(row)
        print("bottom==================")
        for row in bottomM:
            print(row)

        return res




class Solution:
    def pacificAtlantic(self, matrix):
        def inRange(i,j):
            return 0 <= i < row and 0 <= j < col
        res = []
        if not matrix:
            return res
        row = len(matrix)
        if type(matrix[0]) is int:
            return matrix
        col = len(matrix[0])
        pacific = set()
        atlantic = set()
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    pacific.add((i,j))
                if i == row - 1 or j == col - 1:
                    atlantic.add((i,j))
        p_set = set([p for p in pacific])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while pacific:
            p2 = set()
            for i,j in pacific:
                for di,dj in directions:
                    ti,tj = i+di, j+dj
                    if inRange(ti, tj) and (ti, tj) not in p_set and matrix[ti][tj] >= matrix[i][j]:
                        p2.add((ti, tj))
            pacific = p2
            # print(p2)
            p_set |= p2
        # print(p_set)
        a_set = set([a for a in atlantic])
        while atlantic:
            a2 = set()
            for i,j in atlantic:
                for di,dj in directions:
                    ti,tj = i+di, j+dj
                    if inRange(ti, tj) and (ti, tj) not in a_set and matrix[ti][tj] >= matrix[i][j]:
                        a2.add((ti, tj))
            atlantic = a2
            a_set |= a2
        # print(a_set)
        res = p_set & a_set
        return [list(k) for k in res]


class Solution:
    def pacificAtlantic(self, matrix):
        def inRange(i,j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i,j,visited):
            visited[i][j] = 1
            for di,dj in directions:
                ti,tj = i+di, j+dj
                if inRange(ti,tj) and not visited[ti][tj] and matrix[ti][tj] >= matrix[i][j]:
                    dfs(ti,tj,visited)

        if not matrix:
            return []
        if type(matrix[0]) is int:
            return matrix
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m, n = len(matrix), len(matrix[0])
        p_visited = [[0]*n for _ in range(m)]
        a_visited = [[0]*n for _ in range(m)]
        res = []
        for i in range(m):
            dfs(i,0,p_visited)
            dfs(i,n-1,a_visited)
        for j in range(n):
            dfs(0,j,p_visited)
            dfs(m-1,j,a_visited)
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])
        return res


from collections import deque
class Solution:
    def pacificAtlantic(self, matrix):
        def inRange(i,j):
            return 0 <= i < m and 0 <= j < n
        if not matrix:
            return []
        if type(matrix[0]) is int:
            return matrix
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m, n = len(matrix), len(matrix[0])
        def bfs(points):
            dq = deque(points)
            while dq:
                i,j = dq.popleft()
                for di,dj in directions:
                    ti,tj = di+i, dj+j
                    if inRange(ti,tj) and (ti,tj) not in points and matrix[ti][tj] >= matrix[i][j]:
                        dq.append((ti,tj))
                        points.add((ti,tj))
            return points
        pacific = set([(i,0) for i in range(m)] + [(0,j) for j in range(1,n)])
        atlantic = set([(i, n-1) for i in range(m)] + [(m-1,j) for j in range(n-1)])
        return list(bfs(pacific) & bfs(atlantic))




S = Solution()
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1,],[6,7,1,4,5,],[5,1,1,2,4,]]
print(S.pacificAtlantic(matrix))
matrix = []
print(S.pacificAtlantic(matrix))
matrix = [2]
print(S.pacificAtlantic(matrix))