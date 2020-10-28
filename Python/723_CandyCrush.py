"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.

 

Example:

Input:
board =
[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

Output:
[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

Explanation:

 

Note:

The length of board will be in the range [3, 50].
The length of board[i] will be in the range [3, 50].
Each board[i][j] will initially start as an integer in the range [1, 2000].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy-crush
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def candyCrush(self, board):
        R, C = len(board), len(board[0])
        #  add extra 0s for board
        board2 = [[0]*(C+2)]
        for _row in board:
            board2.append([0] + _row + [0])
        board2.append([0]*(C+2))

        t_board = [list(row) for row in zip(*board2)]  # transpose of matrix
        # for row in t_board:
        #     print(row)

        crush_nodes = set()
        while True:
            for i in range(1, C+1):
                for j in range(1, R+1):
                    if t_board[i-1][j] == t_board[i][j] == t_board[i+1][j] != 0:
                        crush_nodes |= {(i,j),(i-1,j),(i+1,j)}
                    if t_board[i][j-1] == t_board[i][j] == t_board[i][j+1] != 0:
                        crush_nodes |= {(i,j),(i,j-1),(i,j+1)}

            if not crush_nodes:
                break
            # print('crush_nodes', crush_nodes)
            for i, j in crush_nodes:
                t_board[i][j] = 0
            crush_nodes = set()
            for i, _row in enumerate(t_board):
                tmp = [v for v in _row if v != 0]
                t_board[i] = (R+1-len(tmp))*[0] + tmp + [0]

            # print('++++++++++++++++')
            # for row in t_board:
            #     print(row)
            # print('++++++++++++++++')
        res = [list(row[1:-1]) for row in zip(*t_board)][1:-1]
        # for row in res:
        #     print(row)
        return res


class Solution:
    def candyCrush(self, board):
        def crushNodes(matrix):
            """
            crush nodes in matrix
            """
            nodes = set()
            r, c = len(matrix), len(matrix[0])
            for i in range(1, r-1):
                for j in range(1, c-1):
                    if matrix[i-1][j] == matrix[i][j] == matrix[i+1][j] != 0:
                        nodes |= {(i,j),(i-1,j),(i+1,j)}
                    if matrix[i][j-1] == matrix[i][j] == matrix[i][j+1] != 0:
                        nodes |= {(i,j),(i,j-1),(i,j+1)}
            return nodes

        def update(matrix, nodes):
            """
            change value of nodes in matrix to 0, then update the matrix
            """
            r, c = len(matrix), len(matrix[0])
            for i, j in nodes:
                matrix[i][j] = 0
            for i, row in enumerate(matrix):
                tmp = [v for v in row if v != 0]
                matrix[i] = (c-1-len(tmp))*[0] + tmp + [0]


        R, C = len(board), len(board[0])
        #  add extra 0s for board,so we do not need to consider the out of border issue
        board2 = [[0]*(C+2)]
        for _row in board:
            board2.append([0] + _row + [0])
        board2.append([0]*(C+2))

        t_board = [list(row) for row in zip(*board2)]  # transpose of the board

        crush_nodes = crushNodes(t_board)
        while len(crush_nodes) > 0:
            update(t_board, crush_nodes)
            crush_nodes = crushNodes(t_board)

        res = [list(row[1:-1]) for row in zip(*t_board)][1:-1] # transpose of t_board and got the orginal updated board
        return res



# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/candy-crush/solution/fen-sui-tang-guo-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def candyCrush(self, board):
        R, C = len(board), len(board[0])
        todo = False
        # print('++++++++++++++++')
        # for row in board:
        #     print(' '.join(((4-len(v))*' ' + (v)) for v in map(str, row)))
            # (row)

        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    todo = True

        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    todo = True

        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

        return self.candyCrush(board) if todo else board


S = Solution()
board =[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
print(S.candyCrush(board))