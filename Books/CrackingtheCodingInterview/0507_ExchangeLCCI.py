"""
配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。

示例1:

 输入：num = 2（或者0b10）
 输出 1 (或者 0b01)
示例2:

 输入：num = 3
 输出：3
提示:

num的范围在[0, 2^30 - 1]之间，不会发生整数溢出。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/exchange-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def exchangeBits(self, num: int) -> int:
        bin_num = bin(num)[2:]
        if len(bin_num) % 2 == 1:
            bin_num = '0' + bin_num
        res = ''
        for i in range(len(bin_num) // 2):
            res += bin_num[i * 2 + 1] + bin_num[i * 2]
        return int(res, 2)


S = Solution()
print(S.exchangeBits(2))
print(S.exchangeBits(3))