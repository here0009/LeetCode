"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""
class Solution_1:
    def countBattleships(self, board) -> int:
        def dfs(i,j):
            visited[i][j] = 1
            if i+1 < m and board[i+1][j] == 'X':
                dfs(i+1,j)
            if j+1 < n and board[i][j+1] == 'X':
                dfs(i,j+1)


        
        res = 0
        m,n = len(board), len(board[0])
        visited = [[0]*n for _ in range(m)]
        # print(visited) 
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and board[i][j] == 'X':
                    print(i,j)
                    dfs(i,j)
                    res += 1
        return res

class Solution:
    def countBattleships(self, board) -> int:
        """
        make only the start ship counts, if the left or upper is a 'X', it would not counts
        """
        res = 0
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] != 'X') and (j == 0 or board[i][j-1] != 'X'):
                    res += 1
        return res



s = Solution()
board = ['X..X', '...X', '...X']
print(s.countBattleships(board))