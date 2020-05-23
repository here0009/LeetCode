"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""
class Solution:
    def calculate(self, s: str) -> int:
        v_stack = []
        sign_stack = []
        index = 0
        values = '0123456789'
        while index < len(s):
            v = s[index]
            start_index = index
            if v in values:
                while index+1 < len(s) and v[index+1] in values:
                    index += 1
                v_stack.append(int(v[start_index:index]))
            elif v in '+-':
                sign_stack.append(v)
            elif v in '*/':
                m = v_stack.pop()
                while s[index] not in values:
                    index += 1
                n = int(s[index])
                if v == '*':
                    v_stack.append(m*n)
                elif v == '/':
                    v_stack.append(m//n)
            index += 1
        # print(v_stack)
        # print(sign_stack)
        if len(v_stack) == 1:
            return v_stack[0]
        else:
            while sign_stack:
                sign = sign_stack.pop()
                m = v_stack.pop()
                n = v_stack.pop()
                if sign == '+':
                    v_stack.append(m+n)
                elif sign == '-':
                    v_stack.append(m-n)
        return v_stack[0]
                
s = Solution()
# print(s.calculate("3+2*2"))

# print(s.calculate(" 3/2 "))
# print(s.calculate(" 3+5 / 2 "))
print(s.calculate("42"))
# print(s.calculate("3+2*2"))

