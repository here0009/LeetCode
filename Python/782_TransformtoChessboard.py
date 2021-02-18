"""
An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.

What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If the task is impossible, return -1.

Examples:
Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation:
One potential sequence of moves is shown below, from left to right:

0110     1010     1010
0110 --> 1010 --> 0101
1001     0101     1010
1001     0101     0101

The first move swaps the first and second column.
The second move swaps the second and third row.


Input: board = [[0, 1], [1, 0]]
Output: 0
Explanation:
Also note that the board with 0 in the top left corner,
01
10

is also a valid chessboard.

Input: board = [[1, 0], [1, 0]]
Output: -1
Explanation:
No matter what sequence of moves you make, you cannot end with a valid chessboard.
Note:

board will have the same number of rows and columns, a number in the range [2, 30].
board[i][j] will be only 0s or 1s.
"""
# 01010011
# 10101100
# 01010011

# 11100
# 10011
# 11100


from typing import List
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        """
        Thoughts:
        we can use binary number to represent each row in board, and use bfs to check if we can reach the final state
        for each state, we got N*(N - 1) next state
        suppose we can swap any two cell in board, the total state is N!, 30! ~ 10**39 is too much
        wrong answer
        """
        N = len(board)
        total = sum(sum(row) for row in board)
        if total != N **2 // 2:
            return -1
        mid, rmd = divmod(N, 2)
        t1 = int('10' * mid + '1' * rmd, 2)
        t2 = int('01' * mid + '0' * rmd, 2)
        print(bin(t1), bin(t2))
        t_row1 = tuple([t1, t2] * mid + [t1] * rmd)
        t_row2 = tuple([t2, t1] * mid + [t2] * rmd)
        print(t1, t2, t_row1, t_row2)
        step = 0
        visited = set()
        bfs = [start]

# https://leetcode.com/problems/transform-to-chessboard/discuss/440085/Python-detailed-explanation
class Solution_1:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        if n <= 1:
            return 0
        rows = [''.join(str(c) for c in r) for r in board]
        counter = Counter(rows)
        keys = list(counter)  # keys are the patterns of rows in board, such as 11100, 00011
        if len(keys) != 2 or abs(counter[keys[0]] - counter[keys[1]]) > 1 or abs(keys[0].count('1') - keys[0].count('0')) > 1 or any(a == b for a, b in zip(*keys)):
            return -1
        rowdiff = sum(board[0][i] != (i % 2) for i in range(n))
        coldiff = sum(board[i][0] != (i % 2) for i in range(n))
        if rowdiff % 2 != 0 or (n % 2 == 0 and (n - rowdiff) < rowdiff):
            rowdiff = n - rowdiff
        if coldiff % 2 != 0 or (n % 2 == 0 and (n - coldiff) < coldiff):
            coldiff = n - coldiff
        return (rowdiff + coldiff) // 2

from typing import List
from collections import Counter
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        """
        there are some requirements for a board to transform to a chessboard
        1. the sum of a row/col must be N//2 or N//2 + 1
        for example.
        if a row/col is 11111, no matter how we swap, we can not transform this row/col to be valid
        so a row/col should have N//2 or N//2 + 1 of '1's
        2. there should 2 kind of row/col pattern, and they should be opposite
        for exmple
        11100
        10110
        no matter how we swap, we can not transform it to a chessboard
        but we can transform the following board to a chess board easily
        11100
        00011
        """
        def sumstr(string):
            return sum(int(i) for i in string)
        N = len(board)
        if N <= 1:
            return 0
        row_pattern = Counter([(''.join(str(i) for i in row)) for row in board])
        keys = list(row_pattern.keys())
        if len(keys) != 2 or abs(row_pattern[keys[0]] - row_pattern[keys[1]]) > 1 or abs(sumstr(keys[0]) - sumstr(keys[1])) > 1 or any(a == b for a, b in zip(keys[0], keys[1])):
            return -1
        row_diff = sum([board[0][i] != i % 2 for i in range(N)])  # if we want board[0][0] to be 0, then board[0][1] is 1, calculate how many need to swap
        col_diff = sum([board[i][0] != i % 2 for i in range(N)])
        if row_diff % 2 != 0 or (N % 2 == 0 and N - row_diff < row_diff):  # if the cols need to swap is odd, we can to swap need to reverse it and make it even. so we can use row_diff//2 swaps to make it
            row_diff = N - row_diff
        if col_diff % 2 != 0 or (N % 2 == 0 and N - col_diff < col_diff):
            col_diff = N - col_diff
        return (row_diff + col_diff) // 2

  
S = Solution_1()

board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
print(S.movesToChessboard(board))

board = [[0, 1], [1, 0]]
print(S.movesToChessboard(board))

board = [[1, 0], [1, 0]]
print(S.movesToChessboard(board))

board = [[1,0,0],[0,1,1],[1,0,0]]
print(S.movesToChessboard(board))
