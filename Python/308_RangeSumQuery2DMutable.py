"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


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
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-2d-mutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class NumMatrix:

    def __init__(self, matrix):


    def update(self, row: int, col: int, val: int) -> None:


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

# 作者：frankchen250
# 链接：https://leetcode-cn.com/problems/range-sum-query-2d-mutable/solution/python-zi-dian-by-frankchen250-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None

        self.m = len(matrix)
        self.n = len(matrix[0])
        self.dp = [[0]*(self.n+1) for _ in range(self.m+1)]
        self.data = matrix
        self.update_val = {}

        # dp计算累加和
        for i in range(self.m):
            for j in range(self.n):
                self.dp[i+1][j+1] = self.dp[i][j+1] + self.dp[i+1][j] - self.dp[i][j] + matrix[i][j]

    def update(self, row: int, col: int, val: int) -> None:
        self.update_val[(row, col)] = val - self.data[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]

        for i, j in self.update_val:
            if i >= row1 and i <= row2 and j >= col1 and j <= col2:
                res += self.update_val[(i, j)]
        return res

# 作者：TheWizard
# 链接：https://leetcode-cn.com/problems/range-sum-query-2d-mutable/solution/ji-yi-zi-ju-zhen-he-zeng-liang-xiu-gai-by-thewizar/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.n = len(matrix)
        self.m = len(matrix[0]) if self.n > 0 else 0
        self.sumv = [[0 for _ in range(self.m+1)] for _ in range(self.n+1)]
        for i in range(1, self.n+1):
            for j in range(1, self.m+1):
                self.sumv[i][j] = (self.mat[i-1][j-1] + self.sumv[i-1][j] + self.sumv[i][j-1] - self.sumv[i-1][j-1])

    def update(self, row: int, col: int, val: int) -> None:
        oldv = self.mat[row][col]
        self.mat[row][col] = val
        d = val - oldv
        for i in range(row+1, self.n+1):
            for j in range(col+1, self.m+1):
                self.sumv[i][j] += d

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2, col2 = row2 + 1, col2 + 1
        res = self.sumv[row2][col2] - self.sumv[row1][col2] - self.sumv[row2][col1] + self.sumv[row1][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

