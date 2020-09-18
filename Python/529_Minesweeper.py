"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

 

Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
"""

"""
Thoughts:
digits will not be recursively revealed
because M is surrounded by digit, it won't be revealed either
"""

from collections import Counter
class Solution:
    def updateBoard(self, board, click):
        def inRange(i,j):
            return i>=0 and i<R and j>=0 and j<C

        def dfs(i,j):
            visited[i][j] = 1
            if (i,j) in adj_mines:
                board[i][j] = str(adj_mines[(i,j)])
                return
            board[i][j] = 'B'
            for di,dj in dir_8:
                if inRange(i+di, j+dj) and visited[i+di][j+dj] == 0:
                    dfs(i+di, j+dj)

        dir_8 = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        dir_4 = [(0,1),(0,-1),(1,0),(-1,0)]
        click = tuple(click)
        mines = set()
        adj_mines = Counter()
        R, C = len(board), len(board[0])
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'M':
                    mines.add((i,j))
                    for di,dj in dir_8:
                        if inRange(i+di, j+dj):
                            adj_mines[(i+di,j+dj)] += 1
        p, q = click
        if click in mines:
            board[p][q] = 'X'
            return board
        if click in adj_mines:
            board[p][q] = str(adj_mines[(p,q)])
            return board
        visited = [[0]*C for _ in range(R)]
        dfs(p,q)
        # for row in board:
        #     print(row)
        return board


class Solution:      
    def updateBoard(self, A, click):
        click = tuple(click)
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for dr in xrange(-1, 2):
                for dc in xrange(-1, 2):
                    if (dr or dc) and 0 <= r + dr < R and 0 <= c + dc < C:
                        yield r + dr, c + dc

        stack = [click]
        seen = {click}
        while stack:
            r, c = stack.pop()
            if A[r][c] == 'M':
                A[r][c] = 'X'
            else:
                mines_adj = sum( A[nr][nc] in 'MX' for nr, nc in neighbors(r, c) )
                if mines_adj:
                    A[r][c] = str(mines_adj)
                else:
                    A[r][c] = 'B'
                    for nei in neighbors(r, c):
                        if A[nei[0]][nei[1]] == 'E' and nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
        return A
s = Solution()
# board = [['E', 'E', 'E', 'E', 'E'],['E', 'E', 'M', 'E', 'E'],['E', 'E', 'E', 'E', 'E'],['E', 'E', 'E', 'E', 'E']]
# click =  [0,4]
# board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]

# click = [3,0]
# print(s.updateBoard(board,click))

# board = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]

# click = [1,2]
# print(s.updateBoard(board,click))
board =[["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]
print("______________")
for row in board:
    print(row)
print("______________")
click =[0,0]
output = [["B","B","B","B","B","B","1","E"],["B","1","1","1","B","B","1","M"],["1","E","M","1","B","B","1","1"],["M","E","1","1","B","B","B","B"],["1","1","B","B","B","B","B","B"],["B","B","B","B","B","B","B","B"],["B","1","2","2","1","B","B","B"],["B","1","M","M","1","B","B","B"]]
expected = [["B","B","B","B","B","B","1","E"],["B","1","1","1","B","B","1","M"],["1","2","M","1","B","B","1","1"],["M","2","1","1","B","B","B","B"],["1","1","B","B","B","B","B","B"],["B","B","B","B","B","B","B","B"],["B","1","2","2","1","B","B","B"],["B","1","M","M","1","B","B","B"]]
print(s.updateBoard(board,click))

# print("______________")
# for row in output:
#     print(row)
print("______________")
for row in expected:
    print(row)