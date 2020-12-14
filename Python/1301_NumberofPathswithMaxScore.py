"""
You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

 

Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]
Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]
Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]
 

Constraints:

2 <= board.length == board[i].length <= 100
"""


from typing import List
from collections import defaultdict, Counter
class Solution:
    """
    TLE
    """
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        def neighbors(i, j):
            for di,dj in [(0, -1), (-1, 0), (-1, -1)]:
                ni, nj = i + di, j + dj
                if ni >= 0 and nj >= 0 and board[ni][nj] != 'X':
                    yield ni, nj

        def dfs(i, j, pre):
            # print(i, j, pre)
            if board[i][j].isdigit():
                v = (int(board[i][j]) + pre) % M
            else:
                v = pre
            counts[(i, j)][v] += 1
            for ni, nj in neighbors(i, j):
                dfs(ni, nj, v)

        N = len(board)
        M = 10**9 + 7
        counts = defaultdict(Counter)
        dfs(N - 1, N - 1, 0)
        if (0, 0) not in counts:
            return [0, 0]
        # print(counts)
        lst = [(v, i) for v, i in counts[(0, 0)].items()]
        # print(lst)
        lst.sort()
        return list(lst[-1])


from typing import List
from collections import defaultdict, Counter
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        def neighbors(i, j):
            for di,dj in [(0, -1), (-1, 0), (-1, -1)]:
                ni, nj = i + di, j + dj
                if ni >= 0 and nj >= 0 and board[ni][nj] != 'X':
                    yield ni, nj

        def dfs(i, j, pre):
            # print(i, j, pre)
            if board[i][j].isdigit():
                v = (int(board[i][j]) + pre) % M
            else:
                v = pre
            counts[(i, j)][v] += 1
            for ni, nj in neighbors(i, j):
                dfs(ni, nj, v)

        N = len(board)
        M = 10**9 + 7
        counts = defaultdict(Counter)
        dfs(N - 1, N - 1, 0)
        if (0, 0) not in counts:
            return [0, 0]
        # print(counts)
        lst = [(v, i) for v, i in counts[(0, 0)].items()]
        # print(lst)
        lst.sort()
        return list(lst[-1])


from collections import Counter
class Solution:
    """
    TLE
    """
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        def neighbors(i, j):
            for di,dj in [(0, 1), (1, 0), (1, 1)]:
                ni, nj = i + di, j + dj
                if ni < N and nj < N and board[ni][nj] != 'X' and dp[ni][nj] is not None:
                    yield ni, nj

        N = len(board)
        dp = [[None] * N for _ in range(N)]
        dp[N - 1][N - 1] = Counter()
        dp[N - 1][N - 1][0] += 1
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if board[i][j] in 'XS':
                    continue
                val = int(board[i][j]) if board[i][j].isdigit() else 0
                tmp = Counter()
                for ni, nj in neighbors(i, j):
                    tmp += dp[ni][nj]
                dp[i][j] = Counter()
                for _k, _v in tmp.items():
                    dp[i][j][val + _k] = _v
                # print(i, j, dp[i][j])

        # for row in dp:
        #     print(row)
        lst = [(v, i) for v, i in dp[0][0].items()]
        if not lst:
            return [0, 0]
        # print(lst)
        lst.sort()
        return list(lst[-1])

from collections import Counter
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        def neighbors(i, j):
            for di,dj in [(0, 1), (1, 0), (1, 1)]:
                ni, nj = i + di, j + dj
                if ni < N and nj < N and board[ni][nj] != 'X':
                    yield ni, nj

        N = len(board)
        M = 10**9 + 7
        dp = [[[0,0]] * N for _ in range(N)]
        dp[N - 1][N - 1] = [0, 1]
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if board[i][j] in 'XS':
                    continue
                val = int(board[i][j]) if board[i][j].isdigit() else 0
                tmp = Counter()
                key = 0
                for ni, nj in neighbors(i, j):
                    _k, _v = dp[ni][nj]
                    if _v > 0 and val + _k >= key:
                        tmp[val + _k] += _v
                        key = val + _k
                dp[i][j] = [key, tmp[key] % M]
        # for row in dp:
        #     print(row)
        return dp[0][0]

S = Solution()
board = ["E23","2X2","12S"]
print(S.pathsWithMaxScore(board))
board = ["E12","1X1","21S"]
print(S.pathsWithMaxScore(board))
board = ["E11","XXX","11S"]
print(S.pathsWithMaxScore(board))

["E11","XXX","11S"]
