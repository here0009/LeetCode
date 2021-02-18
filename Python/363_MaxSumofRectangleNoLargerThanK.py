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
        """
        wrong answer
        """
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


from typing import List
from bisect import bisect_left, insort
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Thoughts:
        1. transpose matrix to make C > R
        2. use preSum to caluclate the preSum of each row in matrix
        3. for 2 cols, x and y. claluate the gap between them, that is vals
        4. find the max(sum) of vals <= k in vals
        """
        def maxArray(vals):
            # print('vals', vals)
            preSums = [float('inf')]
            res = -float('inf')
            tmp = 0
            for val in vals:
                insort(preSums, tmp)
                tmp += val
                i = bisect_left(preSums, tmp - k)
                # print(preSums, i, len(preSums), tmp)
                res = max(res, tmp - preSums[i])
                    # print('res1', res, preSum - vals[i])
                # print('res2', res)
            return res

        R, C = len(matrix), len(matrix[0])
        # if R > C:  # make C bigger than R
        #     matrix = [list(zip(*row)) for row in matrix]
        #     R, C = C, R
        for i in range(R):
            for j in range(1, C):
                matrix[i][j] += matrix[i][j - 1]
        res = -float('inf')
        # for row in matrix:
        #     print(row)
        for c1 in range(C):
            for c2 in range(c1, C):
                vals = [matrix[i][c2] - (matrix[i][c1 - 1] if c1 > 0 else 0) for i in range(R)]
                # print(c1, c2, vals)
                res = max(res, maxArray(vals))
        return res


from typing import List
from bisect import bisect_left, insort
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Thoughts:
        1. transpose matrix to make C > R
        2. use preSum to caluclate the preSum of each row in matrix
        3. for 2 cols, x and y. claluate the gap between them, that is vals
        4. find the max(sum) of vals <= k in vals
        """
        def maxArray(vals):
            preSums = [float('inf')]
            res = -float('inf')
            tmp = 0
            for val in vals:
                insort(preSums, tmp)
                tmp += val
                i = bisect_left(preSums, tmp - k)
                res = max(res, tmp - preSums[i])
            return res

        R, C = len(matrix), len(matrix[0])
        # if R < C:  # make C smaller than R
        #     # matrix = [list(zip(*row)) for row in matrix]
        #     matrix = [list(row) for row in zip(*matrix)]
        #     R, C = C, R
        for i in range(R):
            for j in range(1, C):
                matrix[i][j] += matrix[i][j - 1]
        res = -float('inf')
        for c1 in range(C):
            for c2 in range(c1, C):
                vals = [matrix[i][c2] - (matrix[i][c1 - 1] if c1 > 0 else 0) for i in range(R)]
                res = max(res, maxArray(vals))
        return res


S = Solution()
matrix = [[1,0,1],[0,-2,3]]
k = 2
print(S.maxSumSubmatrix(matrix, k))
matrix = [[2,2,-1]]
k = 3
print(S.maxSumSubmatrix(matrix, k))
matrix = [[2,2,-1]]
k = 2
print(S.maxSumSubmatrix(matrix, k))
# Output
# -1
# Expected
# 2
matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
k = 10
print(S.maxSumSubmatrix(matrix, k))
# Output
# 9
# Expected
# 10
matrix = [[7,7,4,-6,-10],[-7,-3,-9,-1,-7],[9,6,-3,-7,7],[-4,1,4,-3,-8],[-7,-4,-4,6,-10],[1,3,-2,3,-10],[8,-2,1,1,-8]]
k = 12
print(S.maxSumSubmatrix(matrix, k))