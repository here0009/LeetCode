"""
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

 

Example 1:



Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
Example 2:



Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
Example 4:

Input: matrix = [[0,0],[0,0]]
Output: 0
Explanation: As there are no 1s, no submatrix of 1s can be formed and the area is 0.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m * n <= 105
matrix[i][j] is 0 or 1.
"""


from typing import List
from collections import defaultdict
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        rows = defaultdict(set)
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 1:
                    rows[i].add(j)
        res = 0
        for i in range(R):
            cols = rows[i]
            res = max(res, len(cols))
            for j in range(i + 1, R):
                # print(cols)
                cols &= rows[j]
                if not cols or len(cols) * (R - i) <= res:
                    break
                res = max(res, len(cols) * (j - i + 1))
        return res


from collections import defaultdict
class Solution_1:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        res = 0
        for i in range(R):
            for j in range(C):
                if i > 0 and matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]
            curr = sorted(matrix[i], reverse=True)
            for k, num in enumerate(curr):
                res = max(res, num * (k + 1))
        return res

from collections import defaultdict
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        rows = defaultdict(set)
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 1:
                    rows[i].add(j)
        res = 0
        for i in range(R):
            cols = rows[i]
            j = i
            while cols and len(cols) * (R - i) > res:
                res = max(res, len(cols) * (j - i + 1))
                j += 1
                cols &= rows[j]
        return res

S = Solution()
matrix = [[0,0,1],[1,1,1],[1,0,1]]
print(S.largestSubmatrix(matrix))
matrix = [[1,0,1,0,1]]
print(S.largestSubmatrix(matrix))
matrix = [[1,1,0],[1,0,1]]
print(S.largestSubmatrix(matrix))
matrix = [[0,0],[0,0]]
print(S.largestSubmatrix(matrix))