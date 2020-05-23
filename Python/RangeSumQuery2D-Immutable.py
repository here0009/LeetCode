"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
class NumMatrix:
    """
    Thought: use an accumulated matirx
    so the result is right-bottom + left-top - top-right - left-bottom
    """

    def __init__(self, matrix):
        if matrix is None or not matrix:
            return
        self.acc_matrix = [[0]*self.c for _ in range(self.r)]
        
        for i in range(self.r):
            for j in range(self.c):
                self.acc_matrix[i][j] = matrix[i][j]

        for i in range(1,self.r): #1st col
            self.acc_matrix[i][0] += self.acc_matrix[i-1][0]
        for j in range(1,self.c): #1st row
            self.acc_matrix[0][j] += self.acc_matrix[0][j-1]
        for i in range(1,self.r):
            for j in range(1,self.c):
                self.acc_matrix[i][j] += self.acc_matrix[i-1][j] + self.acc_matrix[i][j-1] - self.acc_matrix[i-1][j-1] 
        # for row in self.acc_matrix:
        #     print(row)

    def get_val(self,i,j):
        if i<0 or j<0 : #or (i==0 and j==0)
            return 0
        else:
            return self.acc_matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.r == 0 or self.c == 0:
            return 0
        return self.get_val(row2, col2) + self.get_val(row1-1, col1-1) - self.get_val(row2, col1-1) - self.get_val(row1-1, col2)


class NumMatrix:

    def __init__(self, matrix):
        if matrix is None or not matrix:
            return
        self.row,self.col = len(matrix), len(matrix[0])
        self.acc_matrix = [[0]*(self.col+1) for _ in range(self.row+1)]
        for i in range(1,self.row+1):
            for j in range(1,self.col+1):
                self.acc_matrix[i][j] = matrix[i-1][j-1] + self.acc_matrix[i-1][j] + self.acc_matrix[i][j-1] - self.acc_matrix[i-1][j-1]
        # for row in self.acc_matrix:
        #     print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.row == 0 or self.col ==0:
            return 0
        return self.acc_matrix[row2+1][col2+1] + self.acc_matrix[row1][col1] - self.acc_matrix[row1][col2+1] - self.acc_matrix[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Your NumMatrix object will be instantiated and called as such:
matrix = [[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],[1, 2, 0, 1, 5],[4, 1, 0, 1, 7],[1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))

matrix = [[]]
obj = NumMatrix(matrix)
print(obj.sumRegion(0,0,0,0))

# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
# matrix = [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],
# [2,1,4,3],[1,1,2,2],[1,2,2,4]]