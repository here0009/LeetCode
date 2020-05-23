"""
Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
 

Note:

1 <= matrix.length <= 300
1 <= matrix[0].length <= 300
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
"""
class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        """
        Thoughts: if maxtrix_a-maxtrix_b == target, then there is a submatrix in a,b that equals to target
        """
        counters = {}
        res  = 0
        r, c = len(matrix), len(matrix[0])
        sum_rows = [[0]*c for i in range(r)]
        sum_cols = [[0]*c for i in range(r)]

        for i in range(r):
            for j in range(c):
                if i > 0:
                    sum_rows[i][j] = sum_rows[i-1][j] + matrix[i][j]
                else:
                    sum_rows[i][j] = matrix[i][j]
                tmp = sum_rows[i][j]
                if tmp >= target:
                    counters[tmp-target] = counters.get(tmp-target,0)+1
                    res += counters[tmp-target]
                if j > 0:
                    sum_cols[i][j] = sum_cols[i][j-1] + matrix[i][j]
                else:
                    sum_cols[i][j] = matrix[i][j]

        print(sum_rows)
        print(sum_cols)
        return res

class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        """
        Thoughts: if maxtrix_a-maxtrix_b == target, then there is a submatrix in a,b that equals to target
        """
        res = 0
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                if i > 0:
                    matrix[i][j] += matrix[i-1][j]

        # print(matrix)
        for i in range(r):
            for j in range(i,r):
                counters = {0:1}
                tmp_sum = 0
                for k in range(c):
                    if i > 0:
                        tmp_sum += matrix[j][k] - matrix[i-1][k]
                    else:
                        tmp_sum += matrix[j][k]
                    if tmp_sum-target in counters:
                        res += counters[tmp_sum-target]
                    counters[tmp_sum] = counters.get(tmp_sum,0)+1
                # print(counters)
        return res

s = Solution()
matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0
print(s.numSubmatrixSumTarget(matrix, target))
matrix = [[1,-1],[-1,1]]
target = 0
print(s.numSubmatrixSumTarget(matrix, target))
