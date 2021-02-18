"""
给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sorted-matrix-search-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def search_submatrix(p, q):
            # print(p, q)
            if p == q:
                return matrix[p[0]][p[1]] == target
            pi, pj = p
            qi, qj = q
            if qi < pi or qj < pj:
                return False
            mid_i = (pi + qi) // 2
            mid_j = (pj + qj) // 2
            mid_v = matrix[mid_i][mid_j]
            if mid_v == target:
                return True
            elif mid_v > target:
                return search_submatrix(p, (mid_i, mid_j)) or search_submatrix((pi, mid_j + 1), (mid_i, qj)) or search_submatrix((mid_i + 1, pj), (qi, mid_j))
            else:
                return search_submatrix((mid_i + 1, mid_j + 1), q) or search_submatrix((pi, mid_j + 1), (mid_i, qj)) or search_submatrix((mid_i + 1, pj), (qi, mid_j))

        if not matrix:
            return False
        # for row in matrix:
        #     print(row)
        R, C = len(matrix), len(matrix[0])
        return search_submatrix((0, 0), (R - 1, C - 1))

S = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(S.searchMatrix(matrix, 5))
print(S.searchMatrix(matrix, 20))
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(S.searchMatrix(matrix, 5))