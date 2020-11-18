"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def subgrid(i, j):
            i, j = i//3*3, j//3*3
            res = []
            for k in range(i, i+3):
                res.extend(board[k][j:j+3])
            # print('res',i,j,res)
            return res

        def solve(index):
            # if self.res:
            #     return
            if index == 81:
                return True
            i, j = divmod(index, 9)
            if board[i][j] != '.':
                return solve(index+1)
            exsit = set(board[i])|set(trans_board[j])|set(subgrid(i,j))
            possbile = digits -exsit
            # print(index,'e,p',exsit, possbile)
            # # print(index, )
            # print('+++++++')
            # print(index)
            # for row in board:
            #     print(row)
            # print('+++++++')
            # if not possbile:
            #     return
            for d in possbile:
                board[i][j] = d
                trans_board[j][i] = d
                if solve(index+1):
                    return True
                board[i][j] = '.'
                trans_board[j][i] = '.'
            return False
                # board[i][j] = '.'

        # for row in board:
        #     print(row)
        # print('===============')

        digits = set([str(i) for i in range(1,10)])
        trans_board = [list(row) for row in zip(*board)]
        # self.res = False
        solve(0)
        # for row in trans_board:
        #     print(row)
        # print('===============')
        # for row in board:
        #     print(row)



from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def subgrid(i, j):
            i, j = i//3*3, j//3*3
            res = []
            for k in range(i, i+3):
                res.extend(board[k][j:j+3])
            return res

        def solve(index):
            if index == 81:
                return True
            i, j = divmod(index, 9)
            if board[i][j] != '.':
                return solve(index+1)
            exsit = set(board[i])|set(trans_board[j])|set(subgrid(i,j))
            possbile = digits - exsit
            for d in possbile:
                board[i][j] = d
                trans_board[j][i] = d
                if solve(index+1):
                    return True
                board[i][j] = '.'
                trans_board[j][i] = '.'
            return False

        digits = set([str(i) for i in range(1,10)])
        trans_board = [list(row) for row in zip(*board)]
        solve(0)

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def check(x, y, s):
            for i in range(9):
                if board[i][y] == s or board[x][i] == s:
                    return False
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    if board[x//3*3+i][y//3*3+j] == s:
                        return False
            return True
        
        def bt(cur):
            if cur == 81:
                return True
            x, y = cur // 9, cur % 9
            if board[x][y] != '.':
                return bt(cur + 1)
            for i in range(1, 10):
                s = str(i)
                if check(x, y, s):
                    board[x][y] = s
                    if bt(cur + 1):
                        return True
                    board[x][y] = '.'
            return False
        bt(0)


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/sudoku-solver/solution/jie-shu-du-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。    
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def flip(i: int, j: int, digit: int):
            line[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff # 0x1ff is bin:111111111, same as (1<<9)-1
            while mask:
                digitMask = mask & (-mask)
                digit = bin(digitMask).count("0") - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1) #eliminate the last '1'
                if valid:
                    return
            
        line = [0] * 9
        column = [0] * 9
        block = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)

        dfs(0)



S = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(S.solveSudoku(board))

