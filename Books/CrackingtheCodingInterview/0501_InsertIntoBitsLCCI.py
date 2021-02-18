"""
给定两个整型数字 N 与 M，以及表示比特位置的 i 与 j（i <= j，且从 0 位开始计算）。

编写一种方法，使 M 对应的二进制数字插入 N 对应的二进制数字的第 i ~ j 位区域，不足之处用 0 补齐。具体插入过程如图所示。



题目保证从 i 位到 j 位足以容纳 M， 例如： M = 10011，则 i～j 区域至少可容纳 5 位。

 

示例1:

 输入：N = 1024(10000000000), M = 19(10011), i = 2, j = 6
 输出：N = 1100(10001001100)
示例2:

 输入： N = 0, M = 31(11111), i = 0, j = 4
 输出：N = 31(11111)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-into-bits-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        bin_N, bin_M = bin(N)[2:][::-1], bin(M)[2:]
        string = bin_N[j + 1:][::-1]+ '0' *(j - i + 1 - len(bin_M)) + bin_M + bin_N[:i][::-1]
        # print((j - i - len(bin_M)))
        return int(string, 2)

class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        bin_N, bin_M = bin(N)[2:][::-1], bin(M)[2:][::-1]
        string = bin_N[:i] + bin_M + '0' *(j - i + 1 - len(bin_M)) + bin_N[j + 1:]
        return int(string[::-1], 2)


S = Solution()
print(S.insertBits(1024, 19, 2, 6))
print(S.insertBits(0, 31, 0, 4))
print(S.insertBits(2032243561, 10, 24, 29))
# 输出：
# 706843497
# 预期结果：
# 1243714409
print(bin(706843497))
print(bin(1243714409))