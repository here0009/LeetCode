"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""
"""
Thoughts: seed and expand
collapse the matrix until only one row or col
"""
class Solution_1:
    def countSquares(self, matrix) -> int:
        """
        TLE
        """
        res = 0
        m, n = len(matrix), len(matrix[0])
        while m > 1 and n > 1:
            res += sum(sum(row) for row in matrix)
            matrix_2 = [[0]*(n-1) for _ in range(m-1)]
            for i in range(m-1):
                for j in range(n-1):
                    if sum([matrix[i][j], matrix[i+1][j], matrix[i][j+1], matrix[i+1][j+1]]) == 4:
                        matrix_2[i][j] = 1
                    else:
                        matrix_2[i][j] = 0
            # for row in matrix_2:
            #     print(row)
            matrix = matrix_2
            m, n = len(matrix), len(matrix[0])
        res += sum(sum(row) for row in matrix)
        return res

"""
Thoughts: using dp[i][j] to record the number of squares than can be formed by i,j as its bottom-right index. so dp[i][j] equals to 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) 
"""
class Solution:
    def countSquares(self, A):
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    continue
                if i == 0 or j == 0:
                    res += A[i][j]
                else:
                    A[i][j] = 1 + min(A[i-1][j], A[i][j-1], A[i-1][j-1])
                    res += A[i][j]
        # for row in A:
        #     print(row)
        return res


s = Solution()
matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
print(s.countSquares(matrix))

matrix = [[1,0,1],[1,1,0],[1,1,0]]

print(s.countSquares(matrix))
