"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
class Solution:
    def searchLine(self, line, target):
        print(line)
        if not line:
            return False
        middle = len(line)//2
        if target == line[middle]:
            return True
        elif target < line[middle]:
            return self.searchLine(line[:middle], target)
        else:
            return self.searchLine(line[middle+1:], target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0] or target is None:
            return False
        if type(matrix[0]) != list:
            if matrix[0] == target:
                return True
            else:
                return False
        m, n = len(matrix), len(matrix[0])
        row_0 = matrix[0]
        col_0 = [i[0] for i in matrix]
        row_break_flag = False
        col_break_flag = False
        for row_index, row in enumerate(row_0):
            if row > target:
                row_break_flag = True
                break
        if row_break_flag:
            row_index -= 1
        else:
            row_index = n-1

        for col_index, col in enumerate(col_0):
            if col > target:
                col_break_flag = True
                break

        if col_break_flag:
            col_index -= 1
        else:
            col_index = m-1
        return self.searchLine(matrix[col_index], target) or self.searchLine([i[row_index] for i in matrix], target)

import bisect
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0] or target is None:
            return False
        if matrix[0] == target or matrix[0][0] == target:
            return True

        col_n = bisect.bisect_left(matrix[0], target)-1
        col_0 = [row[0] for row in matrix]
        row_n = bisect.bisect_left(col_0, target)-1
        row = matrix[row_n][:col_n+1]
        col_t = bisect.bisect_left(row,target)
        
        col = [row[col_n] for row in matrix[:row_n+1]]
        row_t = bisect.bisect_left(col,target)
        # print(row[col_t])
        # print(col[row_t])
        # print(row)
        # print(col)
        return row[col_t] == target or col[row_t] == target


class Solution:
    def searchMatrix(self, matrix, target):
        if matrix:
            row,col = len(matrix), len(matrix[0])
            m, n = row-1, 0 #start from southwest point
            while m >= 0 and n < col:
                if matrix[m][n] == target:   
                    return True
                elif matrix[m][n] > target: #target smaller than current val, go north
                    m -= 1
                else:
                    n += 1 #target larger than current val, go east, do not go south, because all the south value are larger than target(already checked)
        return False


# matrix = [[1,   4,  7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]]
# target = 5
# print(matrix[:][2])
# print(matrix[2])
# print([i[2] for i in matrix])

s = Solution()
matrix = [[1,   4,  7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]]
target = 5
print(s.searchMatrix(matrix, target))
target = 20
print(s.searchMatrix(matrix, target))

matrix = [[1]]
target = 1
print(s.searchMatrix(matrix, target))

matrix = [[]]
target = 1
print(s.searchMatrix(matrix, target))

matrix = [[1]]
target = 1
print(s.searchMatrix(matrix, target))

matrix = [[1]]
target = 2
print(s.searchMatrix(matrix, target))

matrix = [[1,3,5]]
target = 5
print(s.searchMatrix(matrix, target))

# matrix = [[1,4],[2,5]]
# target = 5
# print(s.searchMatrix(matrix, target))

# matrix = [[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]]
# target = 13
# print(s.searchMatrix(matrix, target))
# for line in matrix:
#     print(line)