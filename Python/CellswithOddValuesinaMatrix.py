"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

 

Example 1:


Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
Example 2:


Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
 

Constraints:

1 <= n <= 50
1 <= m <= 50
1 <= indices.length <= 100
0 <= indices[i][0] < n
0 <= indices[i][1] < m
"""
class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        matrix = [[0]*m for _ in range(n)]
        for r,c in indices:
            for k in range(m):
                matrix[r][k] += 1
            for k in range(n):
                matrix[k][c] += 1
        res = 0
        for row in matrix:
            res += sum(t%2 for t in row)
        return res

s = Solution()
n = 2
m = 3
indices = [[0,1],[1,1]]
print(s.oddCells(n,m,indices))


n = 2
m = 2
indices = [[1,1],[0,0]]
print(s.oddCells(n,m,indices))