"""
给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。

示例 1：

输入: num = 1775(11011101111)
输出: 8
示例 2：

输入: num = 7(0111)
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-bits-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseBits(self, num: int) -> int:
        gap, no_gap, res = 0, 0, 0
        M = (1 << 32)
        if num < 0:
            string = bin(M + num)[2:]
        else:
            string = bin(num)[2:]
        print(string)
        if len(string) < 32:
            string = '0' + string
        else:
            string = string[-32:]
        for i in string:
            if i == '1':
                gap += 1
                no_gap += 1
            else:
                gap, no_gap = no_gap + 1, 0
            res = max(res, gap, no_gap + 1)
        return min(res, 32)

S = Solution()
print(S.reverseBits(1775))
print(S.reverseBits(7))
print(S.reverseBits(-1))