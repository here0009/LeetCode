"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""
"""
Thoughts:
use board[i][j] to store both orginal and next state of board[i][j]
   org  next_state
0   0   0
1   1   0
2   0   1
3   1   1
"""
class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inRange(i,j):
            return i>=0 and i<m and j>=0 and j<n
        def shift(i,j):
            neighbors = 0
            org = board[i][j] % 2
            for dx,dy in directions:
                if inRange(i+dx,j+dy):
                    neighbors += board[i+dx][j+dy] % 2 #store org state in 2^0, next state in 2^1
            if org == 1:
                if neighbors < 2 or neighbors > 3:
                    board[i][j] = 0*2 + org #dies
                else:
                    board[i][j] = 1*2 + org
            else:
                if neighbors == 3:
                    board[i][j] = 1*2 + org

        m, n = len(board), len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        for i in range(m):
            for j in range(n):
                shift(i,j)
        # for row in board:
        #     print(row)
        # print("===================")
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j]//2
        # for row in board:
        #     print(row)

s = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(board)