"""
给你一个大小为 rows x cols 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。

在从左上角 (0, 0) 开始到右下角 (rows - 1, cols - 1) 结束的所有路径中，找出具有 最大非负积 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。

返回 最大非负积 对 109 + 7 取余 的结果。如果最大积为负数，则返回 -1 。

注意，取余是在得到最大积之后执行的。

 

示例 1：

输入：grid = [[-1,-2,-3],
             [-2,-3,-3],
             [-3,-3,-2]]
输出：-1
解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1
示例 2：

输入：grid = [[1,-2,1],
             [1,-2,1],
             [3,-4,1]]
输出：8
解释：最大非负积对应的路径已经用粗体标出 (1 * 1 * -2 * -4 * 1 = 8)
示例 3：

输入：grid = [[1, 3],
             [0,-4]]
输出：0
解释：最大非负积对应的路径已经用粗体标出 (1 * 0 * -4 = 0)
示例 4：

输入：grid = [[ 1, 4,4,0],
             [-2, 0,0,1],
             [ 1,-1,1,1]]
输出：2
解释：最大非负积对应的路径已经用粗体标出 (1 * -2 * 1 * -1 * 1 * 1 = 2)
 

提示：

1 <= rows, cols <= 15
-4 <= grid[i][j] <= 4

You are given a rows x cols matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (rows - 1, cols - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative return -1.

Notice that the modulo is performed after getting the maximum product.

 

Example 1:

Input: grid = [[-1,-2,-3],
               [-2,-3,-3],
               [-3,-3,-2]]
Output: -1
Explanation: It's not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
Example 2:

Input: grid = [[1,-2,1],
               [1,-2,1],
               [3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).
Example 3:

Input: grid = [[1, 3],
               [0,-4]]
Output: 0
Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).
Example 4:

Input: grid = [[ 1, 4,4,0],
               [-2, 0,0,1],
               [ 1,-1,1,1]]
Output: 2
Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).
 

Constraints:

1 <= rows, cols <= 15
-4 <= grid[i][j] <= 4
"""


class Solution:
    def maxProductPath(self, grid) -> int:
        R, C = len(grid), len(grid[0])
        product = [[None]*C for _ in range(R)] # record the max and min product for each grid
        M = 10**9+7
        product[0][0] = [grid[0][0]]
        for i in range(1, R): # initialize 1st col
            product[i][0] = [grid[i][0]*max(product[i-1][0])]
        for j in range(1, C):  # initialize 1st row
            product[0][j] = [grid[0][j]*max(product[0][j-1])]
        for i in range(1, R):
            for j in range(1, C):
                lst = product[i-1][j] + product[i][j-1]
                min_v = min(lst)
                max_v = max(lst) #the min_product and max_product from previouse results
                product[i][j] = [min_v*grid[i][j], max_v*grid[i][j]] 
        v = max(product[-1][-1])
        return v%M if v >= 0 else -1

S = Solution()
grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
print(S.maxProductPath(grid))
grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
print(S.maxProductPath(grid))
grid = [[1, 3],[0,-4]]
print(S.maxProductPath(grid))
grid = [[ 1, 4,4,0],[-2, 0,0,1],[ 1,-1,1,1]]
print(S.maxProductPath(grid))
grid = [[2,1,3,0,-3,3,-4,4,0,-4],[-4,-3,2,2,3,-3,1,-1,1,-2],[-2,0,-4,2,4,-3,-4,-1,3,4],[-1,0,1,0,-3,3,-2,-3,1,0],[0,-1,-2,0,-3,-4,0,3,-2,-2],[-4,-2,0,-1,0,-3,0,4,0,-3],[-3,-4,2,1,0,-4,2,-4,-1,-3],[3,-2,0,-4,1,0,1,-3,-1,-1],[3,-4,0,2,0,-2,2,-4,-2,4],[0,4,0,-3,-4,3,3,-1,-2,-2]]
print(S.maxProductPath(grid))