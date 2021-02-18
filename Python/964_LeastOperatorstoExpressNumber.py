"""
Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /).  For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

The division operator (/) returns rational numbers.
There are no parentheses placed anywhere.
We use the usual order of operations: multiplication and division happens before addition and subtraction.
It's not allowed to use the unary negation operator (-).  For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
We would like to write an expression with the least number of operators such that the expression equals the given target.  Return the least number of expressions used.

 

Example 1:

Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.
Example 2:

Input: x = 5, target = 501
Output: 8
Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8 operations.
Example 3:

Input: x = 100, target = 100000000
Output: 3
Explanation: 100 * 100 * 100 * 100.  The expression contains 3 operations.
 

Note:

2 <= x <= 100
1 <= target <= 2 * 10^8
"""


from functools import lru_cache
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """
        do x*x until x > target
        wrong answer, infinite loop
        """
        @lru_cache(None)
        def calc(num):
            # print(num)
            if num <= 1:
                res = num
            else:
                op = 0
                # if num < x:
                #     print(num, num + (num - 1))
                #     return num + (num - 1)
                y = x
                while y < num:
                    y *= x
                    op += 1
                if y == num:
                    res = op
                res = op + calc(num - y // x)
                if y - num < num:
                    res = min(res, op + 1 + calc(y - num))

            # print(num, res)
            return res

        return calc(target)

import math
class Solution:
    def leastOpsExpressTarget(self, x, k):
        from functools import lru_cache
        cost = lambda i: i if i > 0 else 2
        @lru_cache(None)
        def dfs(target):
            i = math.floor(math.log(target, x))
            if x ** i == target:
                return cost(i)
            ans = cost(i) + dfs(target - x ** i) 
            if x ** (i + 1) < 2 * target:
                ans = min(ans, dfs(x ** (i + 1) - target) + i + 1)
            return ans
        return dfs(k) - 1


from functools import lru_cache
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """
        do x*x until x > target
        """
        @lru_cache(None)
        def calc(num):
            """
            in the calulation process, we should control the incr/decr direction of num, to avoid infinite loop
            """
            if num == 1:
                return 1
            op = 0
            y = x
            while y < num:
                y *= x
                op += 1
            if y == num:
                return op
            if op == 0:  # if power == 0, we use x/x +, 2 operations
                res = 2 + calc(num - y // x)
            else:  # if power > 0, we just need power - 1 operations
                res = op + calc(num - y // x)
            if y - num < num:  # if y - num >= num and we do the loop, it will be end up with a infinite loop
                res = min(res, op + 1 + calc(y - num))
            return res

        return calc(target)


S = Solution()
# x = 3
# target = 19
# print(S.leastOpsExpressTarget(x, target))
# x = 5
# target = 501
# print(S.leastOpsExpressTarget(x, target))
# x = 100
# target = 100000000
# print(S.leastOpsExpressTarget(x, target))
# x = 3
# target = 365
# print(S.leastOpsExpressTarget(x, target))
# # Output
# # 16
# # Expected
# # 17
# x = 4
# target = 5
# print(S.leastOpsExpressTarget(x, target))
x =14
target = 5040
print(S.leastOpsExpressTarget(x, target))