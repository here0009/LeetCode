"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
class Solution_1:
    def solveNQueens(self, n: int):
        res = []
        def dfs(boards, row):
            r_list = []
            if row == n:
                for i in range(n):
                    r_string = ''.join(['Q' if j == boards[i] else '.' for j in range(n)])
                    r_list.append(r_string)
                res.append(r_list)
                return
            for col in range(n):
                for r in range(row):
                    if col == boards[r] or abs(boards[r]-col) == abs(row-r):
                        break
                else:
                    boards[row] = col
                    dfs(boards, row+1)

        dfs([-1]*n, 0)
        return res

class Solution:
    def solveNQueens(self, n: int):
        def backtrack(i):
            if i == n:
                self.res.append(list(board))
            for j in range(n):
                if j not in cols and j-i not in diag and j+i not in off_diag:
                    cols.add(j)
                    diag.add(j-i) #dots on the same diag got the same j-i
                    off_diag.add(j+i) #dots on the same anti_diag got the same j+i
                    board.append('.'*(j)+'Q'+(n-j-1)*'.')
                    backtrack(i+1)
                    board.pop()
                    off_diag.remove(j+i)
                    diag.remove(j-i)
                    cols.remove(j)

        self.res = []
        board = []
        cols = set()
        diag = set()
        off_diag = set()
        backtrack(0)
        return self.res




S = Solution()
n = 4
print(S.solveNQueens(n))