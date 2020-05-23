"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution:
    def searchLine(self,line,target):
        """
        :type matrix: List[int]
        :type target: int
        :rtype: bool
        """
        # print("line")
        # print(line)
        if not line:
            return False
        if len(line) == 1:
            if line[0] == target:
                return True
            else:
                return False
        middle = len(line) // 2
        # print(line[middle], middle)
        if line[middle] == target:
            return True
        elif line[middle] > target:
            return self.searchLine(line[:middle], target)
        else:
            return self.searchLine(line[middle+1:], target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # print("matrix")
        # print(matrix)

        if not matrix or not matrix[0] or target is None:
            return False
        m, n = len(matrix), len(matrix[0])
        middle_row = m // 2
        middle_col = n // 2
        # print(matrix[middle_row][middle_col])
        if target == matrix[middle_row][middle_col]:
            return True
        if target < matrix[middle_row][0]:
            if middle_row == 0:
                return False
            else:    
                return self.searchMatrix(matrix[:middle_row], target)
        if target > matrix[middle_row][n-1]:
            if middle_row == m-1:
                return False
            else:
                return self.searchMatrix(matrix[middle_row+1:], target)
        if target < matrix[middle_row][middle_col] and target >= matrix[middle_row][0]:
            return self.searchLine(matrix[middle_row][0:middle_col], target)
        if target > matrix[middle_row][middle_col] and target <= matrix[middle_row][n-1]:
            return self.searchLine(matrix[middle_row][middle_col:n], target)


s = Solution()
matrix = [[1,3,5,7],[10, 11, 16, 20],[23, 30, 34, 50]]
target = 3
print(s.searchMatrix(matrix, target))

matrix = [[1,3,5,7],[10, 11, 16, 20],[23, 30, 34, 50]]
target = 13
print(s.searchMatrix(matrix, target))

matrix = [[1]]
target = 1
print(s.searchMatrix(matrix, target))

matrix = [[]]
target = 1
print(s.searchMatrix(matrix, target))

# matrix = [1]
# target = 1
# print(s.searchMatrix(matrix, target))

matrix = [[1]]
target = 2
print(s.searchMatrix(matrix, target))

matrix = [[1,3,5]]
target = 5
print(s.searchMatrix(matrix, target))


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 1
print(s.searchMatrix(matrix, target))