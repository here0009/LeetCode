"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution:
    def maximalSquare(self, matrix) -> int:
        """
        wrong answer for matrix[2][2] in the example
        """
        
        # matrix = [int(matrix[i][j]) for i in range(row) for j in range(col)]
        y = [int(c) for c in matrix[0]]
        res = max(y)
        for i in range(1,row):
            x = [int(c) for c in matrix[i]]
            for j in range(col):
                if x[j] == 1:
                    if j > 0:
                        x[j] += x[j-1]
                    y[j] += 1
                    res = max(res, min(y[j], x[j]))
                else:
                    y[j] = 0
            print(x,y)
        return res**2

class Solution:
    def maximalSquare(self, matrix) -> int:
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        if col == 0:
            return 0
        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])

        return max([max(r) for r in matrix])**2


s = Solution()
matrix = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,1,1,1]]
print(s.maximalSquare(matrix))
matrix = [[1]]
print(s.maximalSquare(matrix))
matrix = [[1,1],[1,1]]
print(s.maximalSquare(matrix))

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(s.maximalSquare(matrix))
matrix = [[]]
print(s.maximalSquare(matrix))
matrix = []
print(s.maximalSquare(matrix))