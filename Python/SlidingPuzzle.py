"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
"""
from collections import defaultdict
class Solution:
    def slidingPuzzle(self, board) -> int:
        def inRange(i,j):
            return i>=0 and i<2 and j>=0 and j<3

        def listtostr(bd):
            res = ''
            for row in bd:
                res += ''.join(str(i) for i in row)
            return res

        # for row in board:
        #     print(row)
        index_dict = dict()
        index = 0
        directons = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    start_i, start_j = i,j
                index_dict[index] = (i,j)
                index += 1
        # print(index_dict)
        next_index_dict = defaultdict(list)
        for index in range(6):
            i,j = index_dict[index]
            for di,dj in directons:
                if inRange(i+di, j+dj):
                    next_index_dict[index].append((i+di)*3 + (j+dj))

        start_string = listtostr(board)
        bfs = [start_string]
        # print(bfs)
        visited = set()
        visited.add(start_string)
        res = 0
        target = '123450'
        while bfs:
            # print(bfs)
            bfs2 = []
            for string in bfs:
                if string == target:
                    return res
                zero_index = string.find('0')
                for j in next_index_dict[zero_index]:
                    string_list = list(string)
                    string_list[zero_index], string_list[j] = string_list[j], string_list[zero_index]
                    next_string = ''.join(string_list)
                    if next_string not in visited:
                        bfs2.append(next_string)
                    visited.add(next_string)
            bfs = bfs2
            res += 1
        return -1

S = Solution()
board = [[1,2,3],[4,0,5]]
print(S.slidingPuzzle(board))

board = [[1,2,3],[5,4,0]]
print(S.slidingPuzzle(board))
board = [[4,1,2],[5,0,3]]
print(S.slidingPuzzle(board))
board = [[3,2,4],[1,5,0]]
print(S.slidingPuzzle(board))

