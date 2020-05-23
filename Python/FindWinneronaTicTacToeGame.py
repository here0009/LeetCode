"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

 

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "
Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "
 

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
"""
class Solution:
    def tictactoe(self, moves) -> str:
        def check_list(l,s):
            return all(k==s for k in l)

        def check(gird): 
            for row in grid: #check row
                if check_list(row, 'X'):
                    return 'A'
                elif check_list(row, 'O'):
                    return 'B'
            for j in range(3): #check col
                col = [grid[i][j] for i in range(3)]
                if check_list(col, 'X'):
                    return 'A'
                elif check_list(col, 'O'):
                    return 'B'
            dgl_1 = [grid[i][i] for i in range(3)]
            dgl_2 = [gird[i][3-i-1] for i in range(3)]
            # print(dgl_1)
            # print(dgl_2)
            if check_list(dgl_1, 'X') or check_list(dgl_2, 'X'):
                return 'A'
            elif check_list(dgl_1, 'O') or check_list(dgl_2, 'O'):
                return 'B'
            return 'Draw'

        grid = [[1]*3 for _ in range(3)]
        for index in range(len(moves)):
            i,j = moves[index]
            if index % 2 == 0:
                grid[i][j] = 'X'
            else:
                grid[i][j] = 'O'

        # for row in grid:
        #     print (row)
        res = check(grid)
        if res == 'Draw' and len(moves) < 9:
            return 'Pending'
        else:
            return res

s = Solution()
# moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# print(s.tictactoe(moves))


# moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# print(s.tictactoe(moves))

# moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# print(s.tictactoe(moves))

# moves = [[0,0],[1,1]]
# print(s.tictactoe(moves))

moves = [[0,2],[1,0],[2,2],[1,2],[2,0],[0,0],[0,1],[2,1],[1,1]]
print(s.tictactoe(moves))