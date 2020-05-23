"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inRange(i,j):
            return i>=0 and i<m and j>=0 and j<n

        def onborder(i,j):
            return i == 0 or i == m-1 or j == 0 or j == n-1

        def dfs(i,j):
            visited[i][j] = 1
            flip_list.append((i,j))
            if onborder(i,j):
                flip_flag[0] = False           
            for _x,_y in directions:
                dx,dy = i+_x, j+_y
                if inRange(dx,dy) and not visited[dx][dy] and board[dx][dy] == 'O':
                    dfs(dx,dy)

        if not board:
            return
        m,n = len(board), len(board[0])
        # print(m,n)
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        visited = [[0]*n for _ in range(m)]
        res = []
        for i in range(1,m-1):
            for j in range(1,n-1):
                flip_list = []
                flip_flag = [True]
                if not visited[i][j] and board[i][j] == 'O':
                    dfs(i,j)
                    if flip_flag[0]:
                        res.extend(flip_list)

        for i,j in res:
            board[i][j] = 'X'

        # for row in board:
        #     print(row)

class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        Thoughts: DFS from the border, all 'O's linked to the border will not be changed
        """
        def inRange(i,j):
            return i>=0 and i<m and j>=0 and j<n

        def dfs(i,j):
            visited[i][j] = 1
            board[i][j] = 'S'
            for _i,_j in directions:
                dx,dy = i+_i, j+_j
                if inRange(dx,dy) and not visited[dx][dy] and board[dx][dy] == 'O':
                    dfs(dx,dy)

        if not any(board):
            return
        m,n = len(board), len(board[0])
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[m-1][j] == 'O':
                dfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        for row in board:
            print(row)

        

s = Solution()
board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
print(s.solve(board))

board = [["O","O","O"],["O","O","O"],["O","O","O"]]
print(s.solve(board))

board = [["X"]]
print(s.solve(board))