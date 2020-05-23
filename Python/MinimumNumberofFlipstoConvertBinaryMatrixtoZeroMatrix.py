"""
Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbours of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighboors if they share one edge.

Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

Binary matrix is a matrix with all cells equal to 0 or 1 only.

Zero matrix is a matrix with all cells equal to 0.

 

Example 1:


Input: mat = [[0,0],[0,1]]
Output: 3
Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
Example 2:

Input: mat = [[0]]
Output: 0
Explanation: Given matrix is a zero matrix. We don't need to change it.
Example 3:

Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
Output: 6
Example 4:

Input: mat = [[1,0,0],[1,0,0]]
Output: -1
Explanation: Given matrix can't be a zero matrix
 

Constraints:

m == mat.length
n == mat[0].length
1 <= m <= 3
1 <= n <= 3
mat[i][j] is 0 or 1.
"""
"""
BFS
use bfs to try all the possible combinations, use a string to record the visited state
"""
from collections import deque
class Solution:
    def minFlips(self, mat) -> int:
        def flip(string, index):

            res = list(string)
            row, col = divmod(index, n)
            res[index] = flip_dict[res[index]]
            if col > 0:
                res[index-1] = flip_dict[res[index-1]] #left
            if col < n-1:
                res[index+1] = flip_dict[res[index+1]] #right
            if row > 0:
                res[index-n] = flip_dict[res[index-n]] #up
            if row < m-1:
                res[index+n] = flip_dict[res[index+n]] #down
            return ''.join(res)

        flip_dict = {'1':'0', '0':'1'}
        m, n = len(mat), len(mat[0])
        mat_str = ''.join(str(mat[i][j]) for i in range(m) for j in range(n))
        length = m*n
        target = '0'*length
        bfs = deque([mat_str])
        visited = set(mat_str)
        steps = 0
        if mat_str == target:
            return steps
        
        while len(bfs) > 0:
            # print(bfs)
            bfs_2 = deque()
            steps += 1
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                for i in range(length):
                    next_str = flip(curr, i)
                    if next_str == target:
                        return steps
                    if next_str not in visited:
                        visited.add(next_str)
                        bfs_2.append(next_str)
            bfs = bfs_2
        return -1

s = Solution()

mat = [[0,0],[0,1]]
print(s.minFlips(mat))
mat = [[0]]
print(s.minFlips(mat))
mat = [[1,1,1],[1,0,1],[0,0,0]]
print(s.minFlips(mat))
mat = [[1,0,0],[1,0,0]]
print(s.minFlips(mat))   