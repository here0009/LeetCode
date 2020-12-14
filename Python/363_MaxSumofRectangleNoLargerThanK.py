"""
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""


from typing import List
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        res = -float('inf')
        gridSum = [[0] * (C + 1) for _ in range(R + 1)]
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                gridSum[i][j] = gridSum[i - 1][j] + gridSum[i][j - 1] + gridSum[i - 1][j - 1] + matrix[i - 1][j - 1]
                if gridSum[i][j] <= k:
                    res = max(res, gridSum[i][j])
        for row in gridSum:
            print(row)
        return res

S = Solution()
matrix = [[1,0,1],[0,-2,3]]
k = 2
print(S.maxSumSubmatrix(matrix, k))