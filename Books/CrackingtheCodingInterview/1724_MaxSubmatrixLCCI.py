"""
给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。

返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。

注意：本题相对书上原题稍作改动

示例：

输入：
[
   [-1,0],
   [0,-1]
]
输出：[0,1,0,1]
解释：输入中标粗的元素即为输出所表示的矩阵
 

说明：

1 <= matrix.length, matrix[0].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-submatrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
import heapq
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        preSum = [[0] * (C + 1) for _ in range(R + 1)]
        submatirx = []
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] + matrix[i - 1][j - 1] - preSum[i - 1][j - 1]
                submatirx.append((preSum[i][j], i - 1, j - 1))
        submatirx.sort()
        len_s = len(submatirx)
        max_diff = -float('inf')
        res = None
        for row in preSum:
            print(row)
        print(submatirx)
        """
        wrong answer, the calulation of matrix sum is not right
        """
        for left in range(len_s):
            for right in range(len_s - 1, left, -1):
                left_val, left_i, left_j = submatirx[left]
                right_val, right_i, right_j = submatirx[right]
                if right_val - left_val <= max_diff:
                    break
                if left_i < right_i  and left_j <= right_j:
                    max_diff = max(max_diff, right_val - left_val)
                    res = [left_i, left_j, right_i, right_j]
                    break
        return res


from typing import List
import heapq
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        preSum = [[0] * (C + 1) for _ in range(R + 1)]
        submatirx = []
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] + matrix[i - 1][j - 1] - preSum[i - 1][j - 1]
                submatirx.append((preSum[i][j], i - 1, j - 1))
        submatirx.sort()
        len_s = len(submatirx)
        max_diff = -float('inf')
        res = None
        for row in preSum:
            print(row)
        print(submatirx)
        for left in range(len_s):
            for right in range(len_s - 1, left, -1):
                left_val, left_i, left_j = submatirx[left]
                right_val, right_i, right_j = submatirx[right]
                if right_val - left_val <= max_diff:
                    break
                if left_i < right_i  and left_j <= right_j:
                    max_diff = max(max_diff, right_val - left_val)
                    res = [left_i, left_j, right_i, right_j]
                    break
        return res


from typing import List
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        """
        same method as 363_MaxSumofRectangleNoLargerThanK.py
        """
        def maxArray(vals):
            min_v, min_idx = 0, -1
            curr = 0
            max_v = -float('inf')
            res = [None] * 2
            for i, v in enumerate(vals):
                curr += v
                # if vals == [5, 8, 6]:
                #     print(i, v, max_v, curr, min_v)
                if curr - min_v > max_v:
                    max_v = curr - min_v
                    res = [min_idx + 1, i]
                    # if min_idx == -1:
                    #     res = [i, i]
                    # else:
                    #     res = [min_idx, i]
                if curr < min_v:
                    min_v = curr
                    min_idx = i
            # print('vals', vals)
            # print('res', [max_v] + res)
            return [max_v] + res

        R, C = len(matrix), len(matrix[0])
        # print('++++++++++++++')
        # for row in matrix:
        #     print(row)
        # print('++++++++++++++')
        for i in range(R):
            for j in range(1, C):
                matrix[i][j] += matrix[i][j - 1]
        # print('++++++++++++++')
        # for row in matrix:
        #     print(row)
        # print('++++++++++++++')
        max_v = -float('inf')
        res = [None] * 4
        for c1 in range(C):
            for c2 in range(c1, C):
                vals = [matrix[i][c2] - (matrix[i][c1 - 1] if c1 > 0 else 0) for i in range(R)]
                # print('vals', c1, c2, vals, max_v, res)
                val, r1, r2 = maxArray(vals)
                # print('res', val, r1, r2)
                if val > max_v:
                    res = [r1, c1, r2, c2]
                    # print(val, res)
                    max_v = val
        return res


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        """
        same method as 363_MaxSumofRectangleNoLargerThanK.py
        """
        def maxArray(vals):
            min_v, min_idx = 0, -1
            curr = 0
            max_v = -float('inf')
            res = [None] * 2
            for i, v in enumerate(vals):
                curr += v
                if curr - min_v > max_v:
                    max_v = curr - min_v
                    res = [min_idx + 1, i]
                if curr < min_v:
                    min_v = curr
                    min_idx = i

            return [max_v] + res

        R, C = len(matrix), len(matrix[0])
        for i in range(R):
            for j in range(1, C):
                matrix[i][j] += matrix[i][j - 1]

        max_v = -float('inf')
        res = [None] * 4
        for c1 in range(C):
            for c2 in range(c1, C):
                vals = [matrix[i][c2] - (matrix[i][c1 - 1] if c1 > 0 else 0) for i in range(R)]
                val, r1, r2 = maxArray(vals)
                if val > max_v:
                    res = [r1, c1, r2, c2]
                    max_v = val
        return res


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        """
        same method as 363_MaxSumofRectangleNoLargerThanK.py
        """
        def maxArray(vals):
            min_v, min_idx = 0, 0
            max_v = -float('inf')
            res = [None] * 2
            for i, v in enumerate(vals[1:], 1):
                if v - min_v > max_v:
                    max_v = v - min_v
                    res = [min_idx, i]
                if v < min_v:
                    min_v = v
                    min_idx = i
            return [max_v] + res

        R, C = len(matrix), len(matrix[0])
        preSum = [[0] * (C + 1) for _ in range(R + 1)]
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                preSum[i][j] = matrix[i - 1][j - 1] - preSum[i - 1][j - 1] + preSum[i - 1][j] + preSum[i][j - 1]

        max_v = -float('inf')
        res = [None] * 4
        for c1 in range(C):
            for c2 in range(c1 + 1, C + 1):
                vals = [preSum[i][c2] - preSum[i][c1] for i in range(R + 1)]
                val, r1, r2 = maxArray(vals)
                if val > max_v:
                    res = [r1, c1, r2 - 1, c2 - 1]
                    max_v = val
        return res

S = Solution()
matrix = [[-1,0],[0,-1]]
print(S.getMaxMatrix(matrix))
matrix = [[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]]
print(S.getMaxMatrix(matrix))
# 输出
# [0,3,2,3]
# 预期结果
# [0,0,2,3]
# [[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]]