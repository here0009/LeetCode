"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Follow up: Could you solve the problem without using built-in library functions.

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 6-4 / 2 "
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
Example 4:

Input: s = "(2+6* 3+5- (3*14/7+2)*5)+3"
Output: -12
Example 5:

Input: s = "0"
Output: 0
 

Constraints:

1 <= s <= 104
s consists of digits, '+', '-', '*', '/', '(', ')' and ' '.
s is a valid expression.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import deque
class Solution:
    def cal(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1*n2
        elif op == '/':
            return n1//n2

    def calculate(self, s: str) -> int:
        nums = []
        operators = []
        s = s + ' '
        index, length = 0, len(s)
        curr = ''
        while index < length:
            letter = s[index]
            index += 1
            if letter.isdigit():
                curr += letter
            elif letter == '(':
                r_index = index
                p = 1
                while r_index < length:
                    if s[r_index] == '(':
                        p += 1
                    elif s[r_index] == ')':
                        p -= 1
                    if p == 0:
                        break
                    r_index += 1
                v = self.calculate(s[index: r_index])
                nums.append(v)
                index = r_index + 1
                if len(nums) > 1 and operators and operators[-1] in ['*', '/']:
                        q = nums.pop()
                        p = nums.pop()
                        nums.append(self.cal(p, q, operators.pop()))
            else:
                if curr:
                    nums.append(int(curr))
                    curr = ''
                    if len(nums) > 1 and operators and operators[-1] in ['*', '/']:
                        q = nums.pop()
                        p = nums.pop()
                        nums.append(self.cal(p, q, operators.pop()))
                if letter != ' ':
                    operators.append(letter)
            # print(letter, nums, operators)

        # print(nums)
        # print(operators)
        nums = deque(nums)
        operators = deque(operators)
        # print(nums)
        # print(operators)
        while len(nums) > 1 and operators:
            p = nums.popleft()
            q = nums.popleft()
            nums.appendleft(self.cal(p, q, operators.popleft()))
            # print(s, nums, operators)
        if operators and operators[0] == '-':
            return -nums.pop()
        else:
            return nums.pop()
        # return str str(nums.pop())


class Solution:
    def cal(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1*n2
        elif op == '/':
            return n1//n2

    def calculate(self, s: str) -> int:
        nums = []
        operators = []
        s = s + ' '
        index, length = 0, len(s)
        curr = ''
        while index < length-1:
            letter = s[index]
            index += 1
            if letter.isdigit():
                curr += letter
            elif letter == '(':
                r_index = index
                p = 1
                while r_index < length:
                    if s[r_index] == '(':
                        p += 1
                    elif s[r_index] == ')':
                        p -= 1
                    if p == 0:
                        break
                    r_index += 1
                curr = self.calculate(s[index: r_index])
                index = r_index + 1
            elif letter != ' ':
                operators.append(letter)
            if curr != '' and not s[index].isdigit():
                if nums and operators and operators[-1] in ['*', '/']:
                    nums.append(self.cal(nums.pop(), int(curr), operators.pop()))
                else:
                    nums.append(int(curr))
                curr = ''
            # print(nums, operators)

        nums = nums[::-1]
        operators = operators[::-1]
        if len(nums) == len(operators):  # there is an extra sign before num
            nums.append(0)
        while len(nums) > 1 and operators:
            p = nums.pop()
            q = nums.pop()
            nums.append(self.cal(p, q, operators.pop()))
            # print(nums, operators)
        return nums.pop()


# 作者：1973966917
# 链接：https://leetcode-cn.com/problems/basic-calculator-iii/solution/pythonjian-dan-di-gui-by-1973966917/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from collections import deque
class Solution:
    def calculate(self, s):
        def recur(s):
            stack = []
            sign = '+'
            num = 0
            while len(s) > 0:
                c = s.popleft()
                if c.isdigit():
                    num = 10 * num + int(c)
                if c == '(':
                    num = recur(s)
                # s为空时处理最后一个num和sign
                if c in '+-*/()' or not s:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(int(stack.pop() / num))
                    num = 0
                    sign = c
                if c == ')':
                    break
            return sum(stack)
        return recur(deque(list(s)))



# 作者：sunny-253
# 链接：https://leetcode-cn.com/problems/basic-calculator-iii/solution/fei-di-gui-dan-zhan-jie-fa-by-sunny-253/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from collections import deque
class Solution:
    # Deal with the operations
    def solve(self, operand: int, sign: str, stack: deque) -> int:
        if sign == '+':
            return operand
        elif sign == '-':
            return -operand
        elif sign == '*':
            return stack.pop() * operand
        elif sign == '/':
            return int(stack.pop() / operand)

    def calculate(self, s: str) -> int:
        stack = deque()
        operand = 0
        sign = '+'
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                operand = operand * 10 + int(c)
            elif c == '(':
                stack.append(sign)
                sign = '+'
            else:
                result = self.solve(operand, sign, stack)
                operand = 0
                if c == ')':
                    while isinstance(stack[-1], int):
                        result += stack.pop()
                    sign = stack.pop()

                    operand = self.solve(result, sign, stack)
                    sign = '+'
                else:
                    sign = c
                    stack.append(result)

        last = self.solve(operand, sign, stack)
        stack.append(last)
        return sum(stack)


from collections import deque
class Solution:
    def calculate(self, s):
        def solve(lst):
            stack = []
            sign = '+'
            num = 0
            while lst:
                c = lst.popleft()
                if c.isdigit():
                    num = 10*num + int(c)
                elif c == '(':
                    num = solve(lst)
                if c in '+-*/()' or not lst:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop()*num)
                    elif sign == '/':
                        stack.append(int(stack.pop()/num))
                        # stack.append(stack.pop()//num) can not be used here
                        # -3//4 == -1, but we want 0
                    sign = c
                    num = 0
                # print(lst, stack, num, c)
                if c == ')':
                    break
            return sum(stack)
        return solve(deque(list(s)))

S = Solution()
# s = "1 + 1"
# print(S.calculate(s))
# s = " 6-4 / 2 "
# print(S.calculate(s))
# s = "2*(5+5*2)/3+(6/2+8)"
# print(S.calculate(s))
# s = "(2+6* 3+5- (3*14/7+2)*5)+3"
# print(S.calculate(s))
# s = "0"
# print(S.calculate(s))
s = "1*2-3/4+5*6-7*8+9/10"
print(S.calculate(s))
# 输出：
# 28
# 预期结果：
# -24

# s ="(7)-(0)+(4)"
# print(S.calculate(s))
# s = "-1+4*3/3/3/3"
# print(S.calculate(s))