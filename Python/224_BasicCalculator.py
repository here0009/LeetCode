"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution:
    def calculate(self, string: str) -> int:
        index = 0
        length = len(string)
        flag = 1 # 1 for positive, -1 for negative
        stack = []
        while index < length:
            # print(index, stack)
            if string[index].isdigit():
                left = index
                while index < length and string[index].isdigit():
                    index += 1
                num = int(string[left:index])
                stack.append(flag*num)
            else:
                if string[index] == '+':
                    flag = 1
                elif string[index] == '-':
                    flag = -1
                elif string[index] == '(':
                    if flag == 1:
                        stack.append('(')
                    else:
                        flag = 1
                        stack.append('<') # record the minus sign befor parenthess
                elif string[index] == ')':
                    tmp = 0
                    while stack and stack[-1] not in {'(', '<'}:
                        tmp += stack.pop()
                    if stack.pop() == '<':
                        tmp = -tmp
                    stack.append(tmp)
                index += 1
        return sum(stack)
class Solution:
    def calculate(self, s):
        for ch in ['+', '-', '(', ')']:
            s = s.replace(ch, ' ' + ch + ' ') #we can split s to get num
        print(s)
        print(s.split())
        sign = 1
        stack = [0]
        for token in s.split():
            if token in '+-':
                sign = 1 if token == '+' else -1
            elif token == '(':
                stack.extend([sign, 0])
                sign = 1
            elif token == ')':
                value = stack.pop() * stack.pop()
                stack[-1] += value
            else:
                stack[-1] += sign * int(token)
        return stack[-1]

class Solution:
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, [1]
        # stack only restore the sign
        for i in s+"+":
            # print(i, stack)
            if i.isdigit():
                num = 10*num + int(i)
            elif i in "+-":
                res += num * sign * stack[-1]
                sign = 1 if i=="+" else -1
                num = 0
            elif i == "(":
                stack.append(sign * stack[-1])
                sign = 1
            elif i == ")":
                res += num * sign * stack.pop()
                num = 0
        return res

        
S = Solution()
string = "1 + 1"
print(S.calculate(string))
string = " 2-1 + 2 "
print(S.calculate(string))
string = "(1+(4+5+2)-3)+(6+8)"
print(S.calculate(string))
string = "(1+(4+5+2)-3)+(690+8123)"
print(S.calculate(string))
print(eval("(1+(4+5+2)-3)+(690+8123)"))
string = "1-(5)"
print(S.calculate(string))