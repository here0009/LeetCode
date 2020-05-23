"""
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""
from collections import defaultdict
class Solution:
    def diagonalSort(self, mat):
        m,n = len(mat), len(mat[0])
        res = [[0]*n for _ in range(m)]
        index_dict = defaultdict(list)
        for i in range(m):
            for j in range(n):
                index_dict[i-j].append((i,j))
        for key, index_list in index_dict.items():
            vals = sorted([mat[i][j] for i,j in index_list])
            k = 0
            for i,j in index_list:
                res[i][j] = vals[k]
                k += 1
        return res

from collections import defaultdict
class Solution:
    def diagonalSort(self, mat):
        m,n = len(mat), len(mat[0])
        res = [[0]*n for _ in range(m)]
        diagonal_dict = defaultdict(list)
        for i in range(m):
            for j in range(n):
                diagonal_dict[i-j].append(mat[i][j])
        for d in diagonal_dict:
            diagonal_dict[d] = sorted(diagonal_dict[d], reverse = True)
        for i in range(m):
            for j in range(n):
                res[i][j] = diagonal_dict[i-j].pop()
        return res

S = Solution()
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(S.diagonalSort(mat))

