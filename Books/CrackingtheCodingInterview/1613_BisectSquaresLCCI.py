"""
给定两个正方形及一个二维平面。请找出将这两个正方形分割成两半的一条直线。假设正方形顶边和底边与 x 轴平行。

每个正方形的数据square包含3个数值，正方形的左下顶点坐标[X,Y] = [square[0],square[1]]，以及正方形的边长square[2]。所求直线穿过两个正方形会形成4个交点，请返回4个交点形成线段的两端点坐标（两个端点即为4个交点中距离最远的2个点，这2个点所连成的线段一定会穿过另外2个交点）。2个端点坐标[X1,Y1]和[X2,Y2]的返回格式为{X1,Y1,X2,Y2}，要求若X1 != X2，需保证X1 < X2，否则需保证Y1 <= Y2。

若同时有多条直线满足要求，则选择斜率最大的一条计算并返回（与Y轴平行的直线视为斜率无穷大）。

示例：

输入：
square1 = {-1, -1, 2}
square2 = {0, -1, 2}
输出： {-1,0,2,0}
解释： 直线 y = 0 能将两个正方形同时分为等面积的两部分，返回的两线段端点为[-1,0]和[2,0]
提示：

square.length == 3
square[2] > 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bisect-squares-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        getCenter=lambda x,y,r: [x+r/2,y+r/2]
        getAbc=lambda x1,y1,x2,y2: [y2-y1,x1-x2,y1*x2-y2*x1] if [x1,y1]!=[x2,y2] else [1,0,-x1] #中心重合
        crossY=lambda x:(x,-(a*x+c)/b) if b else (math.inf,math.inf)
        crossX=lambda y:(-(b*y+c)/a,y) if a else (math.inf,math.inf)
        a,b,c=getAbc(*getCenter(*square1),*getCenter(*square2))
        (x1,y1,r1),(x2,y2,r2)=square1,square2
        left,right,bottom,top=min(x1,x2),max(x1+r1,x2+r2),min(y1,y2),max(y1+r1,y2+r2)
        res=[pt for pt in {crossX(bottom),crossY(left),crossX(top),crossY(right)} if left<=pt[0]<=right and bottom<=pt[1]<=top]  # great
        return [v for x,y in sorted(res) for v in [x,y]]

# 作者：yuan-zhi-b
# 链接：https://leetcode-cn.com/problems/bisect-squares-lcci/solution/python3-9xing-dai-ma-liang-zheng-fang-xing-zhong-x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



'''
确定两个正方形中心连成的直线，返回直线和边界的交点，判断一下交点在上下边界还是在左右边界即可
'''

class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        xc1, yc1 = square1[0] + square1[2] / 2, square1[1] + square1[2] / 2
        xc2, yc2 = square2[0] + square2[2] / 2, square2[1] + square2[2] / 2

        x1 = square1[0]
        x2 = square1[0] + square1[2]
        x3 = square2[0]
        x4 = square2[0] + square2[2]

        if xc1 == xc2:
            # 答案是竖直直线
            max_y = max(square1[1] + square1[2], square2[1] + square2[2])
            min_y = min(square1[1], square2[1])
            ans = [xc1, min_y, xc1, max_y]
            return ans

        else:
            k = (yc2 - yc1) / (xc2 - xc1)
            b = yc1 - k * xc1

            y1 = k * x1 + b
            if y1 >= square1[1] and y1 <= square1[1] + square1[2]:
                min_x = min(x1, x3)
                max_x = max(x2, x4)

                return [min_x, k*min_x+b, max_x, k*max_x+b]

            else:
                max_y = max(square1[1] + square1[2], square2[1] + square2[2])
                min_y = min(square1[1], square2[1])

                max_yx = (max_y - b) / k
                min_yx = (min_y - b) / k

                ans = [[max_yx, max_y], [min_yx, min_y]]
                ans.sort()

                return [ans[0][0], ans[0][1], ans[1][0], ans[1][1]]

# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/bisect-squares-lcci/solution/python-qiu-zheng-fang-xing-zhong-xin-lian-jie-de-z/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        """
        1. the line connect the center of two squares will dived both of them to two equal parts.
        2. the resutls is:
        *  the divid line and left/down line
        *  the divid line and right/top line
        """
        x1, y1, r1 = square1
        x2, y2, r2 = square2
        xc1, yc1 = x1 + r1 / 2, y1 + r1 / 2
        xc2, yc2 = x2 + r2 / 2, y2 + r2 / 2
        xmin, xmax = min(x1, x2), max(x1 + r1, x2 + r2)
        ymin, ymax = min(y1, y2), max(y1 + r1, y2 + r2)
        # print(xc1, yc1, xc2, yc2)
        if xc1 == xc2:
            return [xc1, ymin, xc1, ymax]
        if yc1 == yc2:
            return [xmin, yc1, xmax, yc1]
        else:
            k = (yc2 - yc1) / (xc2 - xc1)
            b = yc1 - k * xc1
            points = set()
            res = []
            for x in [xmin, xmax]:
                y = k * x + b
                if ymin <= y <= ymax:
                    points.add((x, y))
            for y in [ymin, ymax]:
                x = (y - b) / k
                if xmin <= x <= xmax:
                    points.add((x, y))
            lst = sorted(list(points))
            for x, y in lst:
                res.extend([x, y])
        return res


S = Solution()
square1 = [-1, -1, 2]
square2 = [0, -1, 2]
print(S.cutSquares(square1, square2))