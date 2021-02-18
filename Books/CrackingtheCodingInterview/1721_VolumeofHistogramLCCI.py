"""
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/volume-of-histogram-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left_vals = []
        right_vals = []
        left_max = -float('inf')
        right_max = -float('inf')
        length = len(height)
        for i in range(length):
            left_max = max(height[i] , left_max)
            right_max = max(height[~i], right_max)
            left_vals.append(left_max)
            right_vals.append(right_max)
        right_vals = right_vals[::-1]
        res = 0
        # print(left_vals)
        # print(right_vals)
        # print(height)
        for i in range(length):
            tmp = min(left_vals[i], right_vals[i])
            if height[i] < tmp:
                res += tmp - height[i]
        return res

S = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(S.trap(height))
