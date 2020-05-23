"""
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

 

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"
 

Constraints:

1 <= target.length <= 100
target consists only of English lowercase letters.
"""
class Solution_1:
    def alphabetBoardPath(self, target: str) -> str:
        def path(start, end):
            res = ''
            s_x,s_y = pos_dict[start]
            e_x,e_y = pos_dict[end]
            if e_x - s_x > 0:
                res += (e_x-s_x)*'D'
            else:
                res += (s_x-e_x)*'U'
            if e_y - s_y > 0:
                res += (e_y-s_y)*'R'
            else:
                res += (s_y-e_y)*'L'
            res += '!'
            return res

        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        pos_dict = dict()
        for i in range(len(board)):
            for j in range(len(board[i])):
                pos_dict[board[i][j]] = (i,j)

        res = ''
        start = 'a'
        for letter in target:
            end = letter
            if start == 'z' and end == 'z':
                res += '!'
            elif end == 'z':
                res += path(start, 'u')[:-1] + 'D!'
            elif start == 'z':
                res += 'U' + path('u',end)
            else:
                res += path(start, end)
            start = end
        return res



class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def path(start, end):
            """
            if we move to 'z', we can move to left, then go down
            if we move from 'z', we can move up, then go right
            then it will not be needed to handle 'z' particulaly
            """
            res = ''
            s_x,s_y = pos_dict[start]
            e_x,e_y = pos_dict[end]
            if e_y < s_y:
                res += (s_y-e_y)*'L'
            if e_x < s_x:
                res += (s_x-e_x)*'U'
            if e_y > s_y:
                res += (e_y-s_y)*'R'
            if e_x > s_x:
                res += (e_x-s_x)*'D'
            res += '!'
            return res

        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        pos_dict = dict()
        for i in range(len(board)):
            for j in range(len(board[i])):
                pos_dict[board[i][j]] = (i,j)

        res = ''
        start = 'a'
        for letter in target:
            res += path(start, letter)
            start = letter
        return res

s = Solution()


target = "leet"
print(s.alphabetBoardPath(target))
#Output: "DDR!UURRR!!DDD!"

target = "code"
print(s.alphabetBoardPath(target))
#Output: "RR!DDRR!UUL!R!"



target = "zdz"
print(s.alphabetBoardPath(target))
# Output:
# "DDDDD!UUUUURRR!DDDDDLLL!"
# Expected:
# "DDDDD!UUUUURRR!DDDDLLLD!"

target = "zz"
print(s.alphabetBoardPath(target))