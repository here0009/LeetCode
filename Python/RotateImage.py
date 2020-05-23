"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
class Solution_1:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        layer = 0
        while layer < n //2:
            up, down, left, right = layer, n-layer-1, layer, n-layer-1
            for i in range(layer, n-1-layer):
                j = n-1-i #j = n-1-layer-i is wrong, for i already contains the information of layer
                # print('layer:',layer)
                # print(i,j,up,down)
                matrix[up][i], matrix[i][right], matrix[down][j], matrix[j][left] = matrix[j][left],matrix[up][i],matrix[i][right], matrix[down][j]
            layer += 1

        for row in matrix:
            print(row)


"""
Basically the idea is to move the point (i,j) to (j,n-i-1)

So first step (reverse) moves (i,j) to (n-i-1,j)
Second step takes the transpose of (n-i-1,j) to get (j,n-i-1) which is the transformation we want.
"""
class Solution:
    def antirotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Thoughts:
        the coordinates of the center of the matrix is (0,0)
        so (i,j) rotate 90 degrees clockwise will be (j,-i), anti-clockwise will be (-j,i)
        that is reverse the matrix first, then swap (i,j) with (j,i)
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            print(row)

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Thoughts:
        the coordinates of the center of the matrix is (0,0)
        so (i,j) rotate 90 degrees clockwise will be (j,-i), anti-clockwise will be (-j,i)
        that is reverse the matrix first, then swap (i,j) with (j,i)
        """
        
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        matrix.reverse()
        for row in matrix:
            print(row)

s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.rotate(matrix))

matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
print(s.rotate(matrix))
