"""
给定一个二维平面及平面上的 N 个点列表Points，其中第i个点的坐标为Points[i]=[Xi,Yi]。请找出一条直线，其通过的点的数目最多。

设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为S，你仅需返回[S[0],S[1]]作为答案，若有多条直线穿过了相同数量的点，则选择S[0]值较小的直线返回，S[0]相同则选择S[1]值较小的直线返回。

示例：

输入： [[0,0],[1,1],[1,0],[2,0]]
输出： [0,2]
解释： 所求直线穿过的3个点的编号为[0,2,3]
提示：

2 <= len(Points) <= 300
len(Points[i]) = 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-line-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import defaultdict
class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:

        def slope(i, j):
            xi, yi = points[i]
            xj, yj = points[j]
            if xi == xj:
                return (float('inf'), xi)
            else:
                k = (yj - yi) / (xj - xi)
                b = yi - k * xi
                return (k, b)

        lines = defaultdict(set)
        length = len(points)
        for i in range(length):
            for j in range(i + 1, length):
                # print(i, j, slope(i, j))
                lines[slope(i, j)] |= {i, j}

        # print(lines)
        res_len = 0
        res = []
        for p in lines.values():
            if len(p) >= res_len:
                lst = sorted(list(p))
                if len(lst) > res_len or lst[:2] < res:
                    res = lst[:2]
                    res_len = len(lst)
        return res


S = Solution()
points = [[0,0],[1,1],[1,0],[2,0]]
print(S.bestLine(points))