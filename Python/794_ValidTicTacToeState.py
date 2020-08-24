"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
"""


class Solution:
    def validTicTacToe(self, board) -> bool:
        x_counts = [0]*8 #0-2 for row, 3-5 for col, 6,7 for diagnols
        o_counts = [0]*8
        x, o = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    x += 1
                    x_counts[i] += 1
                    x_counts[j+3] += 1
                    if i == j:
                        x_counts[6] += 1
                    if i + j == 2:
                        x_counts[7] += 1
                elif board[i][j] == 'O':
                    o += 1
                    o_counts[i] += 1
                    o_counts[j+3] += 1
                    if i == j:
                        o_counts[6] += 1
                    if i + j == 2:
                        o_counts[7] += 1
        # print(board)
        # print(x_counts, o_counts)
        # print(x, o)
        if x > o:
            if x - o > 1 or max(o_counts) ==3:
                return False
        else:
            if x < o or max(x_counts) == 3:
                return False
        if max(x_counts) == 3 and max(o_counts) == 3:
            return False
        return True
        
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(board,c):
            for line in board:
                if line[0]==line[1]==line[2]==c:return True
            for col in range(3):
                if board[0][col]==board[1][col]==board[2][col]==c:return True
            if board[0][0]==board[1][1]==board[2][2]==c:return True
            if board[0][2]==board[1][1]==board[2][0]==c:return True
            return False
        c=collections.Counter(''.join(board))
        xc,oc=c['X'],c['O']
        if xc<oc or xc>oc+1:return False
        if win(board,'X') and oc!=xc-1:return False
        if win(board,'O') and oc!=xc:return False
        return True

S = Solution()
board = ["O  ", "   ", "   "]
print(S.validTicTacToe(board))
board = ["XOX", " X ", "   "]
print(S.validTicTacToe(board))
board = ["XXX", "   ", "OOO"]
print(S.validTicTacToe(board))
board = ["XOX", "O O", "XOX"]
print(S.validTicTacToe(board))
board = ["XXX","OOX","OOX"]
print(S.validTicTacToe(board))
board = ["XXO","XOX","OXO"]
print(S.validTicTacToe(board))