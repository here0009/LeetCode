"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution:
    def spiralOrder(self, matrix):
        """
        Thoughts: pop 1st row of matrix, append to res, then anti-clockwise rotate the matrix, until the matrix is empty
        """
        res = []
        while len(matrix) > 0:
            res.extend(matrix.pop(0))
            # print(res)
            if len(matrix) > 0:
                matrix2 = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))][::-1]
                matrix = matrix2
        return res

class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            if matrix:
                res.extend(matrix.pop(0))
            if matrix and matrix[0]:
                res.extend([row.pop() for row in matrix])
            if matrix:
                res.extend(reversed(matrix.pop()))
            if matrix and matrix[0]:
                res.extend(reversed([row.pop(0) for row in matrix]))
        return res
            

s = Solution()
matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
print(s.spiralOrder(matrix))

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
print(s.spiralOrder(matrix))
