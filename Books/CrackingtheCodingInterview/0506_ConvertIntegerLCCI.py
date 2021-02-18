"""
整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。

示例1:

 输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
 输出：2
示例2:

 输入：A = 1，B = 2
 输出：2
提示:

A，B范围在[-2147483648, 2147483647]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-integer-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        def int_to_str(num):
            if num < 0:
                num = (1 << 32) + num
            return bin(num)[2:]

        bin_A, bin_B = int_to_str(A), int_to_str(B)
        i, j = len(bin_A) - 1, len(bin_B) - 1
        res = 0
        while i >= 0 and j >= 0:
            res += bin_A[i] != bin_B[j]
            i -= 1
            j -= 1
        if i >= 0:
            res += sum([s == '1' for s in bin_A[:i + 1]])
        if j >= 0:
            res += sum([s == '1' for s in bin_B[:j + 1]])
        return res
