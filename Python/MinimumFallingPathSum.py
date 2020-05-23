"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

 

Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""
class Solution_1:
    def minFallingPathSum(self, A) -> int:
        min_row = A[-1][:]
        row, col = len(A), len(A[0])
        for i in range(row-2, -1, -1):
            tmp_row = min_row[:]
            for j in range(col):
                if j == 0:
                    tmp_row[j] = A[i][j] + min(min_row[0:2])
                elif j == col-1:
                    tmp_row[j] = A[i][j] + min(min_row[col-2:col])
                else:
                    tmp_row[j] = A[i][j] + min(min_row[j-1:j+2])
            min_row = tmp_row
        # print(min_row)
        return min(min_row)


class Solution:
    def minFallingPathSum(self, A) -> int:
        row, col = len(A), len(A[0])
        dp = A[0][:]
        for i in range(1,row):
            dp = [A[i][j]+min(dp[max(0,j-1):min(col,j+2)]) for j in range(col)]
        return min(dp)

s = Solution()
A = [[1,2,3],[4,5,6],[7,8,9]]
print(s.minFallingPathSum(A))

A = [[1]]
print(s.minFallingPathSum(A))
