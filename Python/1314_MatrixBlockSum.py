"""
Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
"""


class Solution:
    def matrixBlockSum(self, mat, K: int):
        m, n = len(mat), len(mat[0])
        preSum = [[0]*(n + 1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1,n+1):
                preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] + mat[i-1][j-1] - preSum[i-1][j-1]
        # for row in preSum:
        #     print(row)
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            min_i = max(i-K, 0)+1
            max_i = min(m-1, i+K)+1
            for j in range(n):
                min_j = max(j-K, 0)+1
                max_j = min(n-1, j+K)+1
                res[i][j] = preSum[max_i][max_j] + preSum[min_i-1][min_j-1] - preSum[min_i-1][max_j] - preSum[max_i][min_j-1]
                # print('++',i,j,min_i,max_i, min_j,max_j, preSum[max_i][max_j] , preSum[min_i-1][min_j-1] , preSum[min_i-1][max_j] ,preSum[max_i][min_j-1])
        return res

# https://leetcode.com/problems/matrix-block-sum/discuss/477036/JavaPython-3-PrefixRange-sum-w-analysis-similar-to-LC-30478
class Solution:
    def matrixBlockSum(self, mat, K: int):
        m, n = len(mat), len(mat[0])
        preSum = [[0]*(n + 1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1,n+1):
                preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] + mat[i-1][j-1] - preSum[i-1][j-1]

        res = [[0]*n for _ in range(m)]
        for i in range(m):
            min_i = max(i-K, 0)
            max_i = min(m, i+K+1)
            for j in range(n):
                min_j = max(j-K, 0)
                max_j = min(n, j+K+1)
                res[i][j] = preSum[max_i][max_j] + preSum[min_i][min_j] - preSum[min_i][max_j] - preSum[max_i][min_j]
        return res

S = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
K = 1
print(S.matrixBlockSum(mat, K))

mat = [[1,2,3],[4,5,6],[7,8,9]]
K = 2
print(S.matrixBlockSum(mat, K))