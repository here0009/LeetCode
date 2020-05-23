"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""
from collections import Counter
class Solution:
    def isValidSudoku(self, board) -> bool:
        """
        Thoughts:check rows, cols and subboard individualy
        """
        m,n = len(board), len(board[0])
        for row in board:
            row_counter = Counter([r for r in row if r != '.'])
            # print(row_counter)
            # print(row_counter.most_common())
            if row_counter and row_counter.most_common()[0][1] > 1:
                return False

        for j in range(n):
            col_counter = Counter([board[i][j] for i in range(m) if board[i][j] != '.'])
            # print(col_counter)
            # print(col_counter.most_common())
            if col_counter and col_counter.most_common()[0][1] > 1:
                return False

        for si in range(0,m,3):
            for sj in range(0,n,3):
                subboard_counter = Counter([board[i][j] for i in range(si,si+3) for j in range(sj,sj+3) if board[i][j] != '.'])
                # print(subboard_counter)
                # print(subboard_counter.most_common())
                if subboard_counter and subboard_counter.most_common()[0][1] > 1:
                    return False
        return True


class Solution:
    def isValidSudoku(self, board) -> bool:
        m,n = len(board), len(board[0])
        row_set = [{} for _ in range(m)]
        col_set = [{} for _ in range(n)]
        sub_set = [{} for _ in range(9)]
        for i in range(m):
            for j in range(n):
                num = board[i][j]
                if num != '.':
                    sub_index = i//3*3 + j//3
                    row_set[i][num] = row_set[i].get(num,0) + 1
                    col_set[j][num] = col_set[j].get(num,0) + 1
                    sub_set[sub_index][num] = sub_set[sub_index].get(num,0) + 1
                    if row_set[i][num] > 1 or  col_set[j][num] > 1 or sub_set[sub_index][num] > 1:
                        return False
        return True



S = Solution()
board = [["5","3",".",".","7",".",".",".","."],  ["6",".",".","1","9","5",".",".","."],  [".","9","8",".",".",".",".","6","."],  ["8",".",".",".","6",".",".",".","3"],  ["4",".",".","8",".","3",".",".","1"],  ["7",".",".",".","2",".",".",".","6"],  [".","6",".",".",".",".","2","8","."],  [".",".",".","4","1","9",".",".","5"],  [".",".",".",".","8",".",".","7","9"]]
print(S.isValidSudoku(board))


board = [["8","3",".",".","7",".",".",".","."],  ["6",".",".","1","9","5",".",".","."],  [".","9","8",".",".",".",".","6","."],  ["8",".",".",".","6",".",".",".","3"],  ["4",".",".","8",".","3",".",".","1"],  ["7",".",".",".","2",".",".",".","6"],  [".","6",".",".",".",".","2","8","."],  [".",".",".","4","1","9",".",".","5"],  [".",".",".",".","8",".",".","7","9"]]
print(S.isValidSudoku(board))


board = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
print(S.isValidSudoku(board))