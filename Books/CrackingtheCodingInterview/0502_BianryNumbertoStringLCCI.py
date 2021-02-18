"""
二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。

示例1:

 输入：0.625
 输出："0.101"
示例2:

 输入：0.1
 输出："ERROR"
 提示：0.1无法被二进制准确表示
提示：

32位包括输出中的"0."这两位。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bianry-number-to-string-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def printBin(self, num: float) -> str:
        digits = []
        power = 0
        while num and power < 31:
            k = 1 / 2**power
            if num >= k:
                num -= k
                digits.append('1')
            else:
                digits.append('0')
            power += 1
        # print('{}.{}'.format(digits[0], ''.join(digits[1:])))
        if num:
            return 'ERROR'
        res = '{}.{}'.format(digits[0], ''.join(digits[1:]))
        return res

S = Solution()
num = 0.625
print(S.printBin(num))
num = 0.1
print(S.printBin(num))
