"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(boards,row): #assign boards[index]
            if row == n:
                # print(boards)
                self.res += 1
                return

            for col in range(n): #i for row, boards[i] for col
                for j in range(row): #if row == 0, else will implement
                    if col == boards[j] or abs(boards[j]-col) == abs(j-row):
                        break
                else:
                    # print('boards[row]', row, col)
                    boards[row] = col
                    dfs(boards,row+1)

        boards = [-1]*n
        self.res = 0
        dfs(boards,0)

        return self.res

S = Solution()
n = 4
print(S.totalNQueens(n))
