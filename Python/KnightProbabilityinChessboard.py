"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

 



 

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
 

Note:

N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
"""



class Solution:
    """
    TLE
    """
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def inRange(i,j):
            return 0 <= i < N and 0 <= j < N

        # @lru_cahce(None)
        def dfs(k, i, j):
            res = 0
            if not inRange(i,j):
                return res
            if k == 0:
                return 1
            for di, dj in directions:
                res += 0.125 * dfs(k - 1, i + di, j + dj)
            return res

        directions = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        return dfs(K, r, c)


from functools import lru_cache
class Solution_1:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        def inRange(i,j):
            return 0 <= i < N and 0 <= j < N

        @lru_cache(None)
        def next_pos(i,j):
            return [(i+di, j+dj) for di,dj in directions if inRange(i+di, j+dj)]

        
        def dfs(k, i, j):
            # print(k, i, j)
            res = 0
            if not inRange(i,j):
                return res
            if k == 0:
                return 1
            # k -= 1
            res += 0.125 * sum(dfs(k-1,ni,nj) for ni,nj in next_pos(i,j))
            return res

        directions = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        return dfs(K, r, c)


from collections import defaultdict
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def inRange(i,j):
            return 0 <= i < N and 0 <= j < N

        matrix = [[0]*N for _ in range(N)]
        matrix[r][c] = 1
        directions = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        pre_pos_dict = defaultdict(list)
        for i in range(N):
            for j in range(N):
                for di,dj in directions:
                    if inRange(i+di, j+dj):
                        pre_pos_dict[(i+di, j+dj)].append((i,j))
        while K > 0:
            matrix2 = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    matrix2[i][j] = 0.125 * sum(matrix[ti][tj] for ti,tj in pre_pos_dict[(i,j)])
            matrix = matrix2
            K -= 1
        return sum(sum(row) for row in matrix)


from collections import defaultdict
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def inRange(i,j):
            return 0 <= i < N and 0 <= j < N
        
        memo = {(r,c):1}
        directions = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        
        while K > 0:
            memo2 = defaultdict(int)
            for (i,j), v in memo.items():
                for di,dj in directions:
                    if inRange(i+di, j+dj):
                        memo2[(i+di, j+dj)] += 0.125*v
            memo = memo2
            K -= 1

        return sum(memo.values())

S = Solution()
print(S.knightProbability(3, 2, 0, 0))
print(S.knightProbability(8, 30, 6, 4))
