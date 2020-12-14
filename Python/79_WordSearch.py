"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
class Solution:
    """
    TLE to the last testcase
    """
    def exist(self, board, word) -> bool:
        def inRange(i,j):
            return 0<=i<m and 0<=j<n

        def dfs(i,j,index):
            k = index
            if board[i][j] != word[index]:
                return index-1
            if k == len_w-1: #board[i][j] == word[index]
                # print(i,j,board[i][j])
                return k
            else:
                for di,dj in directions:
                    tmpi,tmpj = i+di, j+dj
                    if inRange(tmpi,tmpj) and visited[tmpi][tmpj] == 0:
                        visited[tmpi][tmpj] = 1
                        k = max(k, dfs(tmpi, tmpj, index+1)) 
                        visited[tmpi][tmpj] = 0
                return k

        m, n, len_w = len(board), len(board[0]), len(word)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        res = -1
        for i in range(m):
            for j in range(n):
                visited = [[0]*n for _ in range(m)]
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    res = max(res, dfs(i,j,0))
        # print(word, res)
        return res == len_w-1


from functools import lru_cache
class Solution:
    def exist(self, board, word) -> bool:
        def neighbors(i, j):
            for di, dj in dir4:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    yield ni, nj

        # @lru_cache(None)  we can not use lru_cache here, because the visited information is different
        def dfs(index, i, j):
            if index == len_w - 1:
                return True
            for ni, nj in neighbors(i, j):
                if visited[ni][nj] == 0 and board[ni][nj] == word[index + 1]:
                    visited[ni][nj] = 1
                    if dfs(index + 1, ni, nj):
                        return True
                    visited[ni][nj] = 0
            return False

        R, C = len(board), len(board[0])
        # print(R, C)
        visited = [[0] * C for _ in range(R)]
        dir4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        len_w = len(word)
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if dfs(0, i, j):
                        return True
                    visited[i][j] = 0
        return False


s = Solution()
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = "ABCCED"
print(s.exist(board, word))

word = "SEE"
print(s.exist(board, word))

word = "ABCB"
print(s.exist(board, word))

board = [["a"]]
word = "a"
print(s.exist(board, word))


board = [["a","a"]]
word = "aaa"
print(s.exist(board, word))

board =[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word ="ABCESEEEFS"
print(s.exist(board, word))  
