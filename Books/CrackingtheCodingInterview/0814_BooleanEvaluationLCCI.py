"""
给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 0 (false)、1 (true)、& (AND)、 | (OR) 和 ^ (XOR) 符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。

示例 1:

输入: s = "1^0|0|1", result = 0

输出: 2
解释: 两种可能的括号方法是
1^(0|(0|1))
1^((0|0)|1)
示例 2:

输入: s = "0&0&0&1^1|0", result = 1

输出: 10
提示：

运算符的数量不超过 19 个

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/boolean-evaluation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import re
from collections import Counter
class Solution:
    def countEval(self, string: str, result: int) -> int:
        def dfs(idx, counts):
            if idx == len_vals:
                return counts

        vals = re.split(r'[&|^]', string)
        print(vals)
        signs = re.split('[01]', string)[1:-1]
        print(signs)
        len_vals = len(vals)



from functools import lru_cache
class Solution:
    def countEval(self, string: str, result: int) -> int:

        def calc(op, l0, l1, r0, r1):
            if op == '&':
                return l0 * r1 + r0 * l1 + r0 * l0, l1 * r1
            if op == '|':
                return l0 * r0, l1 * r1 + l0 * r1 + l1 * r0
            if op == '^':
                return l0 * r0 + l1 * r1, l0 * r1 + l1 * r0


        @lru_cache(None)
        def dp(exp):
            if exp == '1':
                return [0, 1]
            elif exp == '0':
                return [1, 0]
            t0, t1 = 0, 0
            for i, v in enumerate(exp):
                if v not in '^&|':
                    continue
                l0, l1 = dp(exp[:i])
                r0, r1 = dp(exp[i + 1:])
                tmp0, tmp1 = calc(exp[i], l0, l1, r0, r1)
                t0 += tmp0
                t1 += tmp1
            return t0, t1

        t0, t1 = dp(string)
        return [t0, t1][result]


S = Solution()
string = "1^0|0|1"
result = 0
print(S.countEval(string, result))
string = "0&0&0&1^1|0"
result = 1
print(S.countEval(string, result))