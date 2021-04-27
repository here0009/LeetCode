"""
给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。

返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。若无满足条件的子方阵，返回空数组。

示例 1:

输入:
[
   [1,0,1],
   [0,0,1],
   [0,0,1]
]
输出: [1,0,2]
解释: 输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵
示例 2:

输入:
[
   [0,1,1],
   [1,0,1],
   [1,1,0]
]
输出: [0,0,1]
提示：

matrix.length == matrix[0].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-black-square-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from functools import lru_cache
class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        """
        1. 使用res记录结果[i, j, length]
        2. 使用递归函数checkline检测顶点位于i, j， 长度为len_k + 1的两条边， 使用len_k是为了方便下标处理。
        * 如果direction为0, 则i, j为左上角顶点，检测的边为上边界和左边界
        * 如果directtion为1， 则i，j为右下顶点，检测的边为下边界和右边界
        * 使用缓存储存checkline的结果， 这样可以充分利用已有的计算结果。
        3. 遍历i，j， 寻找最大值。
        """

        @lru_cache(None)
        def checkline(i, j, len_x, direction):
            """
            if direction is 0, (i, j) is the top-left corner
            if direction is 1, (i, j) is the bottom-right corner
            """
            if len_x == 0:
                return matrix[i][j] == 0
            if direction == 0:
                if matrix[i + len_x][j] + matrix[i][j + len_x] > 0:
                    return False
            else:
                if matrix[i - len_x][j] + matrix[i][j - len_x] > 0:
                    return False
            return checkline(i, j, len_x - 1, direction)

        length = len(matrix)
        res = [None, None, 0]
        for i in range(length):
            for j in range(length):
                min_len = res[-1]
                for k in range(min_len, length - max(i, j)):
                    if checkline(i, j, k, 0):
                        if checkline(i + k, j + k, k, 1):
                            res = [i, j, k + 1]
                    else:
                        break
        return res if res[-1] != 0 else []



from typing import List
from functools import lru_cache
class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:

        length = len(matrix)
        top_left = [[[0,0] for _ in range(length)] for _ in range(length)]
        bottom_right = [[[0,0] for _ in range(length)] for _ in range(length)]
        for i in range(length - 1, -1, -1):
            for j in range(length - 1, -1, -1):
                if matrix[i][j] == 1:
                    continue
                if i == length - 1:
                    top_left[i][j][0] = 1
                else:
                    top_left[i][j][0] = top_left[i + 1][j][0] + 1
                if j == length - 1:
                    top_left[i][j][1] = 1
                else:
                    top_left[i][j][1] = top_left[i][j + 1][1] + 1

        for i in range(length):
            for j in range(length):
                if matrix[i][j] == 1:
                    continue
                if i == 0:
                    bottom_right[i][j][0] = 1
                else:
                    bottom_right[i][j][0] = bottom_right[i - 1][j][0] + 1
                if j == 0:
                    bottom_right[i][j][1] = 1
                else:
                    bottom_right[i][j][1] = bottom_right[i][j - 1][1] + 1

        res = [None, None, 0]
        for i in range(length):
            for j in range(length):
                min_len = res[-1]
                if min(top_left[i][j]) < min_len:
                    continue
                for k in range(min_len, min(top_left[i][j])):
                    if min(bottom_right[i + k][j + k]) >= k:
                        res = [i, j, k + 1]

        return res if res[-1] != 0 else []



S = Solution()
matrix = [[1,0,1],[0,0,1],[0,0,1]]
print(S.findSquare(matrix))
matrix = [[0,1,1],[1,0,1],[1,1,0]]
print(S.findSquare(matrix))
matrix = [[1]]
print(S.findSquare(matrix))