"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0]*n for _ in range(n)]
        curr = 1
        start = 0
        end = n

        while start < end:
            if start == end-1:
                matrix[start][end-1] = curr
                break
            for j in range(start, end-1): #top
                matrix[start][j] = curr
                curr += 1
            for i in range(start,end-1): #right
                matrix[i][end-1] = curr
                curr += 1
            for j in range(end-1,start,-1): #bottom
                matrix[end-1][j] = curr
                curr += 1
            for i in range(end-1,start,-1): #left
                matrix[i][start] = curr
                curr += 1
            start += 1
            end -= 1

        # for row in matrix:
        #     print(row)

        return matrix

s = Solution()
n = 3
s.generateMatrix(n)

n = 4
s.generateMatrix(n)

n = 5
s.generateMatrix(n)