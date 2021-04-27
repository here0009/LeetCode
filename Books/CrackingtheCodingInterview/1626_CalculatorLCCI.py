"""
给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/calculator-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import deque
class Solution:
    def calculate(self, string: str) -> int:

        idx = 0
        length = len(string)
        nums = deque([])
        ops = deque([])
        while idx < length:
            # print(string[idx], string[idx].isdigit())
            if not string[idx].isdigit():
                if string[idx] != ' ':
                    ops.append(string[idx])
                idx += 1
                continue
            tmp = ''
            while idx < length and string[idx].isdigit():
                tmp += string[idx]
                idx += 1
            nums.append(int(tmp))
            if ops and ops[-1] in {'*', '/'}:
                op = ops.pop()
                n2 = nums.pop()
                n1 = nums.pop()
                if op == '*':
                    nums.append(n1 * n2)
                else:
                    nums.append(n1 // n2)
            # idx += 1
        # print(nums, ops)

        while len(nums) > 1:
            n1 = nums.popleft()
            n2 = nums.popleft()
            op = ops.popleft()
            if op == '+':
                nums.appendleft(n1 + n2)
            else:
                nums.appendleft(n1 - n2)
        return nums.pop()


S = Solution()
string = "3+2*2"
print(S.calculate(string))
string = " 3/2 "
print(S.calculate(string))
string = " 3+5 / 2 "
print(S.calculate(string))
string = "1-1+1"
print(S.calculate(string))
string = "0-2147483647"
print(S.calculate(string))