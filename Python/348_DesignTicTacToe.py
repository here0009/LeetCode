"""
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
Follow up:
Could you do better than O(n2) per move() operation?

 

Example 1:

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
 

Constraints:

2 <= n <= 100
player is 1 or 2.
1 <= row, col <= n
(row, col) are unique for each different call to move.
At most n2 calls will be made to move.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-tic-tac-toe
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TicTacToe:
    """
    TLE
    """
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.win_nums = set()
        matrix = [[0]*n for _ in range(n)]
        for i in range(n):  # change row and col
            matrix[i] = [1]*n
            self.win_nums.add(self.matrixtoInt(matrix))
            self.win_nums.add(self.matrixtoInt(zip(*matrix)))
            matrix[i] = [0]*n
        for i in range(n):
            matrix[i][i] = 1
        self.win_nums.add(self.matrixtoInt(matrix))
        for i in range(n):
            matrix[i][i] = 0
            matrix[i][n-i-1] = 1
        self.win_nums.add(self.matrixtoInt(matrix))
        print(self.win_nums)
        self.p1 = [[0]*n for _ in range(n)]
        self.p2 = [[0]*n for _ in range(n)]

    def check(self, matrix):
        v = self.matrixtoInt(matrix)
        for num in self.win_nums:
            if num & v == num:
                return True
        return False

    def matrixtoInt(self, matrix):
        return int(''.join(''.join(str(num) for num in row) for row in matrix), 2)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            self.p1[row][col] = 1
            if self.check(self.p1):
                return 1
        else:
            self.p2[row][col] = 1
            if self.check(self.p2):
                return 2
        return 0


class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.p1 = [[0]*n for _ in range(3)] # row 1 for row, row 2 for col, matrix[2][0] for diagonal and matrix[2][1] for anti-diagonal
        self.p2 = [[0]*n for _ in range(3)] 

    def check(self, matrix, row, col):
        matrix[0][row] += 1
        matrix[1][col] += 1
        if row == col:
            matrix[2][0] += 1
        if row + col == self.n-1:
            matrix[2][1] += 1
        if max(matrix[0][row], matrix[1][col], matrix[2][0], matrix[2][1]) == self.n:
            return True
        return False

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            if self.check(self.p1, row, col):
                return 1
        else:
            if self.check(self.p2, row, col):
                return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)       


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
# n = 4
# matrix = [[0]*n for _ in range(n)]
# for i in range(n):  # change row and col
#     matrix[i] = [1]*n
#     print(i)
#     print('+++++++++++++++++')
#     for row in matrix:
#         print(row)
#     print('+++++++++++++++++')
#     for row in zip(*matrix):
#         print(row)
#     print('+++++++++++++++++')
#     matrix[i] = [0]*n
    # win_nums.add(self.matrixtoInt(matrix))
    # win_nums.add(self.matrixtoInt(zip(*matrix)))
ticTacToe = TicTacToe(3)
lst = [[0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
for l in lst:
    print(ticTacToe.move(*l))


