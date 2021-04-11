"""
设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-without-plus-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def add(self, a: int, b: int) -> int:
        # ones = 0xffffffff
        ones = (1 << 32) - 1
        a &= ones
        b &= ones
        while b != 0:
            c = a & b
            a ^= b
            b = (c << 1) & ones
        return a if a < (1 << 31) else ~(a ^ ones)

S = Solution()
print(S.add(1, 1))
print(S.add(-1, -1))
print(S.add(-1, 1))
for i in range(31):
    print(i, bin(1 << i))