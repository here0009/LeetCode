"""
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

 

示例：

输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出：3，即数值对(11, 8)
 

提示：

1 <= a.length, b.length <= 100000
-2147483648 <= a[i], b[i] <= 2147483647
正确结果在区间 [0, 2147483647] 内

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-difference-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.extend([-float('inf'), float('inf')])
        b.sort()
        len_b = len(b)
        i = 0
        res = float('inf')
        for num in a:
            while i < len_b and b[i] < num:
                i += 1
            res = min(res, b[i] - num, num - b[i - 1])
        return res

S = Solution()
a = [1, 3, 15, 11, 2]
b = [23, 127, 235, 19, 8]
print(S.smallestDifference(a, b))